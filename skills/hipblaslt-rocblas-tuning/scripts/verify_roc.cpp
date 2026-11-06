// Scoped NMZ/DTK adapter, derived from a previously GPU-validated run.
// See references/validation.md; the portable skill has only been checked offline.
#include <hip/hip_runtime.h>
#include <hip/hip_bfloat16.h>
#include <rocblas/rocblas.h>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <sstream>
#include <stdexcept>
void ck(rocblas_status x){if(x!=rocblas_status_success)throw std::runtime_error("rocblas status="+std::to_string(x));}
void hk(hipError_t x){if(x!=hipSuccess)throw std::runtime_error(hipGetErrorString(x));}
__global__ void fill(hip_bfloat16*p,long n,int seed){for(long i=blockIdx.x*blockDim.x+threadIdx.x;i<n;i+=(long)gridDim.x*blockDim.x){unsigned x=(unsigned)i*1664525u+1013904223u+(unsigned)seed*2654435761u;x^=x>>16;p[i]=hip_bfloat16((float)((int)(x%7)-3));}}
__global__ void reference(const hip_bfloat16*A,const hip_bfloat16*B,const void*D,float*errors,int M,int N,int K,int lda,int ldb,int ldd,long sa,long sb,long sd,int batch,int fp32){
 int s=blockIdx.x;int r=s==0?0:s==1?M-1:(unsigned(s)*15485863u)%M;int c=s==0?0:s==1?N-1:(unsigned(s)*32452843u)%N;int b=s%batch;
 __shared__ float parts[256];float sum=0;for(int k=threadIdx.x;k<K;k+=blockDim.x)sum+=(float)A[b*sa+r*(long)lda+k]*(float)B[b*sb+c*(long)ldb+k];parts[threadIdx.x]=sum;__syncthreads();for(int off=128;off;off/=2){if(threadIdx.x<off)parts[threadIdx.x]+=parts[threadIdx.x+off];__syncthreads();}
 if(threadIdx.x==0){long i=b*sd+c*(long)ldd+r;float expected=fp32?parts[0]:(float)hip_bfloat16(parts[0]);float actual=fp32?((float*)D)[i]:(float)((hip_bfloat16*)D)[i];errors[s]=fabsf(actual-expected);}
}
int main(int argc,char**argv){try{
 if(argc!=5)return 2;int worker=atoi(argv[3]),workers=atoi(argv[4]);if(workers<1||worker<0||worker>=workers)throw std::runtime_error("invalid worker");
 int cold=std::getenv("GEMM_COLD_ITERS")?atoi(std::getenv("GEMM_COLD_ITERS")):3;
 int iters=std::getenv("GEMM_ITERS")?atoi(std::getenv("GEMM_ITERS")):10;
 if(cold<0||iters<1)throw std::runtime_error("invalid timing iterations");
 hk(hipSetDevice(0));rocblas_handle h;ck(rocblas_create_handle(&h));hipStream_t stream;hk(hipStreamCreate(&stream));ck(rocblas_set_stream(h,stream));hipEvent_t st,en;hk(hipEventCreate(&st));hk(hipEventCreate(&en));
 std::ifstream in(argv[1]);std::ofstream out(argv[2]);out<<"family,token_m,us,sampled_values,mismatches,max_abs_error\n";std::string line;int total=0,failures=0;
 while(std::getline(in,line)){
 std::replace(line.begin(),line.end(),',',' ');std::istringstream s(line);int fid,M,K,lda,ldb,ldc,ldd,maxN,batch,fp32;long sa,sb;
 s>>fid>>M>>K>>lda>>ldb>>ldc>>ldd>>maxN>>batch>>sa>>sb>>fp32;
 long asize=(batch-1)*sa+(long)lda*M,bsize=(batch-1)*sb+(long)(maxN-1)*ldb+K;
 hip_bfloat16 *A,*B;void *D;float *err;hk(hipMalloc(&A,asize*2));hk(hipMalloc(&B,bsize*2));hk(hipMalloc(&D,(long)ldd*maxN*batch*(fp32?4:2)));hk(hipMalloc(&err,128*4));fill<<<1024,256,0,stream>>>(A,asize,1);fill<<<1024,256,0,stream>>>(B,bsize,2);
 auto type=fp32?rocblas_datatype_f32_r:rocblas_datatype_bf16_r;float alpha=1,beta=0;
 for(int n=1;n<=maxN;n++){
 if(((n-1)%workers)!=worker)continue;long sd=(long)ldd*n;
 auto run=[&](){if(batch>1)return rocblas_gemm_strided_batched_ex(h,rocblas_operation_transpose,rocblas_operation_none,M,n,K,&alpha,A,rocblas_datatype_bf16_r,lda,sa,B,rocblas_datatype_bf16_r,ldb,sb,&beta,D,type,ldc,sd,D,type,ldd,sd,batch,rocblas_datatype_f32_r,rocblas_gemm_algo_standard,0,0);
 return rocblas_gemm_ex(h,rocblas_operation_transpose,rocblas_operation_none,M,n,K,&alpha,A,rocblas_datatype_bf16_r,lda,B,rocblas_datatype_bf16_r,ldb,&beta,D,type,ldc,D,type,ldd,rocblas_datatype_f32_r,rocblas_gemm_algo_standard,0,0);};
 for(int t=0;t<cold;t++)ck(run());hk(hipEventRecord(st,stream));for(int t=0;t<iters;t++)ck(run());hk(hipEventRecord(en,stream));hk(hipEventSynchronize(en));float ms;hk(hipEventElapsedTime(&ms,st,en));
 reference<<<128,256,0,stream>>>(A,B,D,err,M,n,K,lda,ldb,ldd,sa,sb,sd,batch,fp32);hk(hipStreamSynchronize(stream));float errors[128];hk(hipMemcpy(errors,err,sizeof(errors),hipMemcpyDeviceToHost));int bad=0;float worst=0;for(float e:errors){if(!std::isfinite(e)||e!=0)bad++;worst=std::max(worst,e);}if(bad)failures++;
 out<<fid<<","<<n<<","<<ms*1000/iters<<",128,"<<bad<<","<<worst<<"\n";out.flush();total++;if(n%256==worker+1)std::cout<<"family="<<fid<<" n="<<n<<" total="<<total<<" bad="<<failures<<std::endl;
 }
 hipFree(A);hipFree(B);hipFree(D);hipFree(err);
 }
 std::cout<<"COMPLETE checked="<<total<<" failed="<<failures<<std::endl;return failures?1:0;
 }catch(std::exception&e){std::cerr<<e.what()<<std::endl;return 1;}}
