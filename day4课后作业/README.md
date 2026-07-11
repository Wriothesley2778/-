# Day4 课后作业
## 项目包含
1. task1_data_clean.py：基于Titanic数据集完成数据清洗
- 实现四种缺失值处理：删除行、固定值填充、均值填充、线性插值
- 重复行检测与删除
- 数据类型转换、文本标准化

2. task2_air_analysis.py：基于UCI北京PM2.5数据集做空气质量分析
- 时间序列整理，划分春夏秋冬季节
- 计算污染物均值、标准差、相关性矩阵
- 绘制折线图、柱状图、散点图、相关性热力图
- 分析空气质量季节性变化规律

## 运行依赖
pip install pandas matplotlib numpy seaborn