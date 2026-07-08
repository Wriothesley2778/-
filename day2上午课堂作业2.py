import numpy as np

arr=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print('原始数组：\n',arr)
row2_cols1_3=arr[1,0:3]
print('第二行第1~3列:',row2_cols1_3)
cols3=arr[:,2]
print('所有行第3列：',cols3)
odd_rows=arr[::2,:]
print('奇数行:\n',odd_rows)