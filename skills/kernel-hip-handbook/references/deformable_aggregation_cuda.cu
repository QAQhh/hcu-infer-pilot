#include <ATen/ATen.h>
#include <ATen/cuda/CUDAContext.h>
#include <cuda.h>
#include <cuda_runtime.h>

#include <THC/THCAtomics.cuh>

#include <iostream>
#include <stdlib.h>


__device__ float bilinear_sampling(
    const float *&bottom_data, const int &height, const int &width,
    const int &num_embeds, const float &h_im, const float &w_im,
    const int &base_ptr
) {
  const int h_low = floorf(h_im);
  const int w_low = floorf(w_im);
  const int h_high = h_low + 1;
  const int w_high = w_low + 1;

  const float lh = h_im - h_low;
  const float lw = w_im - w_low;
  const float hh = 1 - lh, hw = 1 - lw;

  const int w_stride = num_embeds;
  const int h_stride = width * w_stride;
  const int h_low_ptr_offset = h_low * h_stride;
  const int h_high_ptr_offset = h_low_ptr_offset + h_stride;
  const int w_low_ptr_offset = w_low * w_stride;
  const int w_high_ptr_offset = w_low_ptr_offset + w_stride;

  float v1 = 0;
  if (h_low >= 0 && w_low >= 0) {
    const int ptr1 = h_low_ptr_offset + w_low_ptr_offset + base_ptr;
    v1 = bottom_data[ptr1];
  }
  float v2 = 0;
  if (h_low >= 0 && w_high <= width - 1) {
    const int ptr2 = h_low_ptr_offset + w_high_ptr_offset + base_ptr;
    v2 = bottom_data[ptr2];
  }
  float v3 = 0;
  if (h_high <= height - 1 && w_low >= 0) {
    const int ptr3 = h_high_ptr_offset + w_low_ptr_offset + base_ptr;
    v3 = bottom_data[ptr3];
  }
  float v4 = 0;
  if (h_high <= height - 1 && w_high <= width - 1) {
    const int ptr4 = h_high_ptr_offset + w_high_ptr_offset + base_ptr;
    v4 = bottom_data[ptr4];
  }

  const float w1 = hh * hw, w2 = hh * lw, w3 = lh * hw, w4 = lh * lw;

  const float val = (w1 * v1 + w2 * v2 + w3 * v3 + w4 * v4);
  return val;
}

struct float2_t{
  float a;
  float b;
};

__forceinline__ __device__
float2_t warp_reduce_sum(float2_t val, int max = 32) {
  for (int offset = max; offset > 0; offset >>= 1 ) {
    val.a += __shfl_down(val.a, offset);
    val.b += __shfl_down(val.b, offset);
  }
  return val;
}

template <int blocksize>
__forceinline__ __device__
float2_t block_reduce_sum(float2_t val, float2_t* shared) {
  const int lid = threadIdx.x % 64;
  const int wid = threadIdx.x / 64;
  constexpr int share_size = blocksize / 64;

  val = warp_reduce_sum(val);

  if constexpr (blocksize == 64) return val;

  if (lid == 0 && wid < share_size) {
    shared[wid] = val;
  }

  __syncthreads();

  if (wid == 0 && lid < share_size) {
    val = shared[lid];
    val = warp_reduce_sum(val, share_size / 2);
  }

  return val;

}

__global__ void deformable_aggregation_kernel_sp(
    const int64_t num_kernels,
    float* output,
    const float* mc_ms_feat,
    const int* spatial_shape,
    const int* scale_start_index,
    const float* sample_location,
    const float* weights,
    int batch_size,
    int num_cams,
    int num_feat,
    int num_embeds,
    int num_scale,
    int num_anchors,
    int num_pts,
    int num_groups
) {
    int64_t block_id = blockIdx.x;   // block -> (batch, anchor)
    int batch_idx = block_id / num_anchors;
    int anchor_local = block_id % num_anchors;
    int anchor_index = batch_idx * num_anchors + anchor_local;

    int channel = threadIdx.x;       // thread -> channel
    if(channel >= num_embeds) return;

    double accum = 0.0;
    // 多维度并行改成了串行遍历
    // 原版本中做一次采样即需要进行一次原子加，现在的版本能减少原子加的次数，1 比 2 少了 (num_pts × num_cams × num_scale) 倍的 atomicAdd

    for(int p=0; p<num_pts; ++p) {
        for(int cam=0; cam<num_cams; ++cam) {
            int loc_offset = (((anchor_index * num_pts + p) * num_cams + cam) << 1);
            float loc_w = sample_location[loc_offset + 0];
            float loc_h = sample_location[loc_offset + 1];
            if(!(loc_w>0.f && loc_w<1.f && loc_h>0.f && loc_h<1.f)) continue;

            for(int s=0; s<num_scale; ++s) {
                int cam_scale_index = cam * num_scale + s;
                int sp_base = cam_scale_index * 2;
                int H = spatial_shape[sp_base + 0];
                int W = spatial_shape[sp_base + 1];

                float h_im = loc_h * H - 0.5f;
                float w_im = loc_w * W - 0.5f;

                int feat_map_idx = batch_idx * num_feat + scale_start_index[cam_scale_index];
                int base_ptr = feat_map_idx * num_embeds + channel;

                float sampled = bilinear_sampling(mc_ms_feat, H, W, num_embeds, h_im, w_im, base_ptr);

                int embeds_per_group = num_embeds / num_groups;
                int group = embeds_per_group>0 ? (channel / embeds_per_group) : 0;
                int w_idx = (((((anchor_index*num_pts + p)*num_cams + cam)*num_scale + s)*num_groups)+group);
                double w_val = double(weights[w_idx]);

                accum += (double)sampled * (double)w_val;
            }
        }
    }
    float result=float(accum);

#ifdef __gfx936__
    __builtin_amdgcn_global_atomic_fadd_f32(output + anchor_index * num_embeds + channel, result);
#else
    atomicAdd(output + anchor_index * num_embeds + channel, result);
#endif
}


__global__ void __launch_bounds__(1024, 1)
deformable_aggregation_kernel(
    const int64_t num_kernels,
    float* output,
    const float* mc_ms_feat,
    const int* spatial_shape,
    const int* scale_start_index,
    const float* sample_location,
    const float* weights,
    int batch_size,
    int num_cams,
    int num_feat,
    int num_embeds,
    int num_scale,
    int num_anchors,
    int num_pts,
    int num_groups
) {
    int64_t idx = blockIdx.x * blockDim.x + threadIdx.x;
    if (idx >= num_kernels) return;

    const float weight = *(weights + idx / (num_embeds / num_groups));
    const int channel_index = idx % num_embeds;
    idx /= num_embeds;
    const int scale_index = idx % num_scale;
    idx /= num_scale;

    const int cam_index = idx % num_cams;
    idx /= num_cams;
    const int pts_index = idx % num_pts;
    idx /= num_pts;

    int anchor_index = idx % num_anchors;
    idx /= num_anchors;
    const int batch_index = idx % batch_size;
    idx /= batch_size;

    anchor_index = batch_index * num_anchors + anchor_index;
    const int loc_offset = ((anchor_index * num_pts + pts_index) * num_cams + cam_index) << 1;

    const float loc_w = sample_location[loc_offset];
    if (loc_w <= 0 || loc_w >= 1) return;
    const float loc_h = sample_location[loc_offset + 1];
    if (loc_h <= 0 || loc_h >= 1) return;

    int cam_scale_index = cam_index * num_scale + scale_index;
    const int value_offset = (batch_index * num_feat + scale_start_index[cam_scale_index]) * num_embeds + channel_index;

    cam_scale_index = cam_scale_index << 1;
    const int h = spatial_shape[cam_scale_index];
    const int w = spatial_shape[cam_scale_index + 1];

    const float h_im = loc_h * h - 0.5;
    const float w_im = loc_w * w - 0.5;

    atomicAdd(
        output + anchor_index * num_embeds + channel_index,
        bilinear_sampling(mc_ms_feat, h, w, num_embeds, h_im, w_im, value_offset) * weight
    );

}

void deformable_aggregation(
    float* output,
    const float* mc_ms_feat,
    const int* spatial_shape,
    const int* scale_start_index,
    const float* sample_location,
    const float* weights,
    int batch_size,
    int num_cams,
    int num_feat,
    int num_embeds,
    int num_scale,
    int num_anchors,
    int num_pts,
    int num_groups
) {
    // new grid: one block per (batch, anchor)
    const int grid = batch_size * num_anchors;

    // choose block threads: try to use a power-of-two near num_embeds but <= 1024
    int threads = 256;
    if (num_embeds <= 128) threads = 128;
    else if (num_embeds < 256) threads = 256;
    else if (num_embeds <= 512) threads = 512;
    else threads = 1024;

    deformable_aggregation_kernel_sp<<< grid, threads >>>(
      0,output, mc_ms_feat, spatial_shape, scale_start_index, sample_location, weights,
        batch_size, num_cams, num_feat, num_embeds, num_scale, num_anchors, num_pts, num_groups
    );

}

void deformable_aggregation_ref(
    float* output,
    const float* mc_ms_feat,
    const int* spatial_shape,
    const int* scale_start_index,
    const float* sample_location,
    const float* weights,
    int batch_size,
    int num_cams,
    int num_feat,
    int num_embeds,
    int num_scale,
    int num_anchors,
    int num_pts,
    int num_groups
) {
    const int64_t num_kernels = (int64_t)batch_size * num_pts * num_embeds * num_anchors * num_cams * num_scale;
    deformable_aggregation_kernel
        <<<(int)ceil(((double)num_kernels/128)), 128>>>(
        num_kernels, output,
        mc_ms_feat, spatial_shape, scale_start_index, sample_location, weights,
        batch_size, num_cams, num_feat, num_embeds, num_scale, num_anchors, num_pts, num_groups
    );
}
