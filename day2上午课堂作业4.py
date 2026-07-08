import numpy as np

#1.生成长度10的随机浮点数组[0,1)，归一化到[0,100]
arr4=np.random.rand(10)
min_val=np.min(arr4)
max_val=np.max(arr4)
normalized=(arr4 - min_val)/(max_val - min_val)*100
print("原始随机数组:",arr4)
print("归一化到 [0,100]:",normalized)

#2.累计和与累计最大值
cumsum=np.cumsum(arr4)
cummax=np.maximum.accumulate(arr4)
print("累计和:",cumsum)
print("累计最大值:",cummax)