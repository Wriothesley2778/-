import numpy as np

#任务1
#逐元素乘法
A=np.random.randint(1,10,(2,3))
P=np.random.randint(1,10,(2,3))
print(A)
print(P)
elementwise_mul=A*P
print('A*B(逐元素)\n',elementwise_mul)
#矩阵乘法
matmul=A@P.T
print('A@P(矩阵乘法):\n',matmul)

#任务2 按行列求和
arr_sum=np.array([[1,2],[3,4]])
row_sum=np.sum(arr_sum,axis=1)
col_sum=np.sum(arr_sum,axis=0)
print("按行求和:", row_sum)
print("按列求和:", col_sum)

#任务3 均值、标准差、四舍五入
arr_float=np.array([1.2, 3.5, 2.8])
mean_val=np.mean(arr_float)
std_val=np.std(arr_float)
rounded=np.round(arr_float)
print("均值:",mean_val)
print("标准差:",std_val)
print("四舍五入:",rounded)

