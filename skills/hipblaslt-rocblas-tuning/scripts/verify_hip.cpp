// Scoped NMZ/DTK adapter, derived from a previously GPU-validated run.
// See references/validation.md; the portable skill has only been checked offline.
#include <hip/hip_runtime.h>
#include <hip/hip_bfloat16.h>
#include <hipblaslt/hipblaslt.h>
#include <hipblaslt/hipblaslt-ext.hpp>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <sstream>
#include <stdexcept>
#include <vector>
void ck(hipblasStatus_t x){if(x!=HIPBLAS_STATUS_SUCCESS)throw std::runtime_error("blas status="+std::to_string(x));}
void hk(hipError_t x){if(x!=hipSuccess)throw std::runtime_error(hipGetErrorString(x));}
__device__ int val(long i,int seed){unsigned x=(unsigned)i*1664525u+1013904223u+(unsigned)seed*2654435761u;x^=x>>16;return (int)(x%7)-3;}
__global__ void fill(signed char*p,long n,int seed){for(long i=blockIdx.x*blockDim.x+threadIdx.x;i<n;i+=(long)gridDim.x*blockDim.x)p[i]=val(i,seed);}
__global__ void scales(float*p,int n){for(int i=blockIdx.x*blockDim.x+threadIdx.x;i<n;i+=gridDim.x*blockDim.x)p[i]=ldexpf(1.f,(i%4)-2);}
__global__ void reference(const signed char*A,const signed char*B,const float*sa,const float*sb,const hip_bfloat16*D,float*errors,int M,int N,int K,int lda,int ldb,int ldd){
 int s=blockIdx.x;int r=s==0?0:s==1?M-1:(unsigned(s)*15485863u)%M;int c=s==0?0:s==1?N-1:(unsigned(s)*32452843u)%N;
 __shared__ int parts[256];int sum=0;for(int k=threadIdx.x;k<K;k+=blockDim.x)sum+=(int)A[r*(long)lda+k]*(int)B[c*(long)ldb+k];parts[threadIdx.x]=sum;__syncthreads();
 for(int offset=128;offset;offset/=2){if(threadIdx.x<offset)parts[threadIdx.x]+=parts[threadIdx.x+offset];__syncthreads();}
 if(threadIdx.x==0){hip_bfloat16 expected((float)parts[0]*sa[r]*sb[c]);errors[s]=fabsf((float)D[c*(long)ldd+r]-(float)expected);}
}
struct Family{int id,M,K,lda,ldb,ldc,ldd,maxN;};
struct Point{int source,index;};
struct Layouts{hipblasLtMatrixLayout_t a,b,c,d;};
int main(int argc,char**argv){try{
 if(argc!=6){std::cerr<<"families.csv points.csv output.csv worker workers\n";return 2;}
 int worker=atoi(argv[4]),workers=atoi(argv[5]);if(workers<1||worker<0||worker>=workers)throw std::runtime_error("invalid worker");
 int cold=std::getenv("GEMM_COLD_ITERS")?atoi(std::getenv("GEMM_COLD_ITERS")):3;
 int iters=std::getenv("GEMM_ITERS")?atoi(std::getenv("GEMM_ITERS")):10;
 if(cold<0||iters<1)throw std::runtime_error("invalid timing iterations");
 hk(hipSetDevice(0));
 std::map<int,Family> families;std::ifstream fs(argv[1]);std::string line;
 while(std::getline(fs,line)){std::replace(line.begin(),line.end(),',',' ');std::istringstream s(line);Family f;s>>f.id>>f.M>>f.K>>f.lda>>f.ldb>>f.ldc>>f.ldd>>f.maxN;families[f.id]=f;}
 std::map<int,std::map<int,Point>> points;std::ifstream ps(argv[2]);
 while(std::getline(ps,line)){std::replace(line.begin(),line.end(),',',' ');std::istringstream s(line);int f,m,idx;s>>f>>m>>idx;points[f][m]={m,idx};}
 hipblasLtHandle_t h;ck(hipblasLtCreate(&h));hipStream_t stream;hk(hipStreamCreate(&stream));hipEvent_t st,en;hk(hipEventCreate(&st));hk(hipEventCreate(&en));
 hipblasLtMatmulPreference_t pref;ck(hipblasLtMatmulPreferenceCreate(&pref));size_t maxws=0;ck(hipblasLtMatmulPreferenceSetAttribute(pref,HIPBLASLT_MATMUL_PREF_MAX_WORKSPACE_BYTES,&maxws,sizeof(maxws)));
 std::ofstream out(argv[3]);out<<"family,token_m,source_m,solution_index,nearest_replaced,baseline_us,tuned_us,speedup,sampled_values,mismatches,max_abs_error,baseline_mismatches,baseline_max_abs_error\n";
 std::map<int,hipblasLtMatmulAlgo_t> cache;int total=0,failures=0;
 for(auto [fid,f]:families){
 signed char *A,*B;int *C;hip_bfloat16*D;float *sa,*sb,*err;
 hk(hipMalloc(&A,(long)f.lda*f.M));hk(hipMalloc(&B,(long)f.ldb*f.maxN));hk(hipMalloc(&C,(long)f.ldc*f.maxN*4));hk(hipMalloc(&D,(long)f.ldd*f.maxN*2));hk(hipMalloc(&sa,f.M*4));hk(hipMalloc(&sb,f.maxN*4));hk(hipMalloc(&err,128*4));
 fill<<<1024,256,0,stream>>>(A,(long)f.lda*f.M,1);fill<<<1024,256,0,stream>>>(B,(long)f.ldb*f.maxN,2);scales<<<256,256,0,stream>>>(sa,f.M);scales<<<256,256,0,stream>>>(sb,f.maxN);hk(hipMemsetAsync(C,0,(long)f.ldc*f.maxN*4,stream));
 hipblasLtMatmulDesc_t desc;ck(hipblasLtMatmulDescCreate(&desc,HIPBLAS_COMPUTE_32I,HIP_R_32F));hipblasOperation_t ta=HIPBLAS_OP_T,tb=HIPBLAS_OP_N;
 ck(hipblasLtMatmulDescSetAttribute(desc,HIPBLASLT_MATMUL_DESC_TRANSA,&ta,sizeof(ta)));ck(hipblasLtMatmulDescSetAttribute(desc,HIPBLASLT_MATMUL_DESC_TRANSB,&tb,sizeof(tb)));
 hipblasLtMatmulMatrixScale_t scale=HIPBLASLT_MATMUL_MATRIX_SCALE_OUTER_VEC_32F;
 ck(hipblasLtMatmulDescSetAttribute(desc,HIPBLASLT_MATMUL_DESC_A_SCALE_MODE,&scale,sizeof(scale)));ck(hipblasLtMatmulDescSetAttribute(desc,HIPBLASLT_MATMUL_DESC_B_SCALE_MODE,&scale,sizeof(scale)));
 ck(hipblasLtMatmulDescSetAttribute(desc,HIPBLASLT_MATMUL_DESC_A_SCALE_POINTER,&sa,sizeof(sa)));ck(hipblasLtMatmulDescSetAttribute(desc,HIPBLASLT_MATMUL_DESC_B_SCALE_POINTER,&sb,sizeof(sb)));
 for(int n=1;n<=f.maxN;n++){
 if(((n-1)%workers)!=worker)continue;
 Layouts l;ck(hipblasLtMatrixLayoutCreate(&l.a,HIP_R_8I,f.K,f.M,f.lda));ck(hipblasLtMatrixLayoutCreate(&l.b,HIP_R_8I,f.K,n,f.ldb));ck(hipblasLtMatrixLayoutCreate(&l.c,HIP_R_32I,f.M,n,f.ldc));ck(hipblasLtMatrixLayoutCreate(&l.d,HIP_R_16BF,f.M,n,f.ldd));
 std::vector<Point> candidates;for(auto [m,p]:points[fid])candidates.push_back(p);std::sort(candidates.begin(),candidates.end(),[n](auto a,auto b){return std::make_pair(abs(a.source-n),a.source)<std::make_pair(abs(b.source-n),b.source);});
 int alpha=1,beta=0;Point chosen{-1,-1};hipblasLtMatmulAlgo_t algo;int replaced=0;
 for(auto p:candidates){if(!cache.count(p.index)){std::vector<int> ids{p.index};std::vector<hipblasLtMatmulHeuristicResult_t> found;ck(hipblaslt_ext::getAlgosFromIndex(h,ids,found));if(found.size()!=1)throw std::runtime_error("index missing");cache[p.index]=found[0].algo;}
 auto a=cache[p.index];size_t ws=0;auto status=hipblaslt_ext::matmulIsAlgoSupported(h,desc,&alpha,l.a,l.b,&beta,l.c,l.d,a,ws);if(status==HIPBLAS_STATUS_SUCCESS&&ws==0){chosen=p;algo=a;break;}replaced++;}
 if(chosen.index<0)throw std::runtime_error("no compatible tuned point f="+std::to_string(fid)+" n="+std::to_string(n));
 hipblasLtMatmulHeuristicResult_t def;int returned=0;ck(hipblasLtMatmulAlgoGetHeuristic(h,desc,l.a,l.b,l.c,l.d,pref,1,&def,&returned));if(!returned)throw std::runtime_error("default missing");
 auto run=[&](hipblasLtMatmulAlgo_t *a){return hipblasLtMatmul(h,desc,&alpha,A,l.a,B,l.b,&beta,C,l.c,D,l.d,a,nullptr,0,stream);};
 auto timing=[&](hipblasLtMatmulAlgo_t *a,bool baseline){for(int t=0;t<cold;t++)ck(run(a));hk(hipEventRecord(st,stream));for(int t=0;t<iters;t++)ck(run(a));hk(hipEventRecord(en,stream));hk(hipEventSynchronize(en));float ms;hk(hipEventElapsedTime(&ms,st,en));return ms*1000/iters;};
 // Alternate order to reduce systematic clock/cache bias.
 float before,after;if(n%2){before=timing(&def.algo,true);after=timing(&algo,false);}else{after=timing(&algo,false);before=timing(&def.algo,true);}
 auto accuracy=[&](hipblasLtMatmulAlgo_t *a){ck(run(a));reference<<<128,256,0,stream>>>(A,B,sa,sb,D,err,f.M,n,f.K,f.lda,f.ldb,f.ldd);hk(hipStreamSynchronize(stream));float errors[128];hk(hipMemcpy(errors,err,sizeof(errors),hipMemcpyDeviceToHost));int bad=0;float worst=0;for(float e:errors){if(!std::isfinite(e)||e!=0)bad++;worst=std::max(worst,e);}return std::make_pair(bad,worst);};
 auto base_accuracy=accuracy(&def.algo);auto tuned_accuracy=accuracy(&algo);int bad=tuned_accuracy.first;float worst=tuned_accuracy.second;if(bad||base_accuracy.first)failures++;
 out<<fid<<","<<n<<","<<chosen.source<<","<<chosen.index<<","<<replaced<<","<<before<<","<<after<<","<<before/after<<",128,"<<bad<<","<<worst<<","<<base_accuracy.first<<","<<base_accuracy.second<<"\n";out.flush();total++;
 hipblasLtMatrixLayoutDestroy(l.a);hipblasLtMatrixLayoutDestroy(l.b);hipblasLtMatrixLayoutDestroy(l.c);hipblasLtMatrixLayoutDestroy(l.d);
 if(n%256==worker+1)std::cout<<"family="<<fid<<" n="<<n<<" total="<<total<<" bad="<<failures<<std::endl;
 }
 hipblasLtMatmulDescDestroy(desc);hipFree(A);hipFree(B);hipFree(C);hipFree(D);hipFree(sa);hipFree(sb);hipFree(err);
 }
 std::cout<<"COMPLETE checked="<<total<<" failed="<<failures<<std::endl;return failures?1:0;
 }catch(std::exception&e){std::cerr<<e.what()<<std::endl;return 1;}}
