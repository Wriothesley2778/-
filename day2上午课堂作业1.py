import numpy as np

arr=np.random.randint(0,10,(3,4))
print('原始数组：\n',arr)#任务一
reshaped_arr=arr.reshape(4,3).T
print('重塑为(4,3)并转置后：\n',reshaped_arr)#任务二
filter_arr=arr[arr>5]
print('大于5的元素',filter_arr)

