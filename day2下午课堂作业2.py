import numpy as np

#任务1：对数收益率
prices=np.array([100,102,105,103,107])
returns=np.log(prices[1:]/prices[:-1])
print("对数收益率:",returns)

#任务2：移动平均线
np.random.seed(42)
#生成100个交易日的随机股价（随机游走）
prices_100=100+np.cumsum(np.random.randn(100))

#5日移动平均线
window=5
ma5=np.convolve(prices_100,np.ones(window)/window,mode='valid')
# 20日移动平均线
window20=20
ma20=np.convolve(prices_100, np.ones(window20)/window20,mode='valid')
print("MA5 (前10个):",ma5[:10])
print("MA20 (前10个):",ma20[:10])

#任务3：风险分析
#生成1000支股票，252个交易日的收益率（假设均值为0，标准差0.01）
returns_data=np.random.randn(1000, 252)*0.01

#年化波动率=标准差 * sqrt(252)
volatility=np.std(returns_data,axis=1)*np.sqrt(252)
#相关系数矩阵(1000x1000)
corr_matrix=np.corrcoef(returns_data)

print("前5支股票年化波动率:",volatility[:5])
print("相关系数矩阵形状:",corr_matrix.shape)