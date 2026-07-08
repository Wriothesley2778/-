import numpy as np
import time

#任务1矩阵乘法性能对比
A=np.random.rand(1000, 2000)
B=np.random.rand(2000, 5000)

t0=time.time();np.dot(A, B);t1=time.time()
t0_2=time.time();A@B;t2=time.time()
t0_3=time.time();np.matmul(A,B);t3=time.time()

print(f"np.dot:{t1-t0:.4f}s,@:{t2-t0_2:.4f}s,np.matmul:{t3-t0_3:.4f}s")

#任务2内存布局影响
arr_c=np.random.rand(1000,1000)               #默认 C 连续（行优先）
arr_f=np.random.rand(1000,1000).copy(order='F')    #F连续（列优先）

t0=time.time();arr_c.sum(axis=1);t_c_row=time.time()-t0
t0=time.time();arr_c.sum(axis=0);t_c_col=time.time()-t0
t0=time.time();arr_f.sum(axis=1);t_f_row=time.time()-t0
t0=time.time();arr_f.sum(axis=0);t_f_col=time.time()-t0

print(f"C连续:行求和{t_c_row:.4f}s,列求和{t_c_col:.4f}s")
print(f"F连续:行求和{t_f_row:.4f}s,列求和{t_f_col:.4f}s")

#任务3：避免临时内存分配
A_small=np.random.rand(100, 100)
result=np.empty_like(A_small)
np.add(np.multiply(A_small, A_small),np.multiply(2, A_small),out=result)
np.add(result, 1, out=result)

print("result前5行5列:\n",result[:5,:5])