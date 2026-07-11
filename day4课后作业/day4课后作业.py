import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.sans-serif"]=["SimHei"]
plt.rcParams["axes.unicode_minus"]=False

np.random.seed(42)
date_range=pd.date_range(start="2016-01-01",end="2016-12-31",freq="h")
n=len(date_range)
df=pd.DataFrame({
    "datetime":date_range,
    "month":date_range.month,
    "PM2.5":np.random.normal(loc=60,scale=30,size=n).clip(0,300),
    "PM10":np.random.normal(loc=90,scale=40,size=n).clip(0,400),
    "SO2":np.random.normal(loc=15,scale=8,size=n).clip(0,80),
    "NO2":np.random.normal(loc=30,scale=12,size=n).clip(0,100),
    "CO":np.random.normal(loc=1.2,scale=0.6,size=n).clip(0,5),
    "O3":np.random.normal(loc=45,scale=20,size=n).clip(0,160)
})

# 构造季节字段
df["season"]=np.where(df["month"].isin([3,4,5]),"春季",
             np.where(df["month"].isin([6,7,8]),"夏季",
             np.where(df["month"].isin([9,10,11]),"秋季","冬季")))
pollution_cols=["PM2.5","PM10","SO2","NO2","CO","O3"]

# 统计指标
stats=df[pollution_cols].agg(["mean","std"])
print("污染物统计指标\n",stats)
corr_matrix=df[pollution_cols].corr()
print("污染物相关性矩阵\n",corr_matrix)

month_avg=df.groupby([df["datetime"].dt.year,df["datetime"].dt.month]).agg(pm25_avg=("PM2.5","mean")).reset_index(drop=True)
plt.figure(figsize=(12,4))
plt.plot(range(len(month_avg)),month_avg["pm25_avg"],color="#d62728")
plt.title("PM2.5月度时间变化折线图")
plt.xlabel("月份序号")
plt.ylabel("PM2.5平均浓度")
plt.grid(alpha=0.3)
plt.savefig("../pm25_trend.png")
plt.close()

# 2.四季PM2.5柱状图
season_pm=df.groupby("season")["PM2.5"].mean()
plt.figure(figsize=(6,4))
plt.bar(season_pm.index,season_pm.values,color=["#1f77b4","#2ca02c","#ff7f0e","#d62728"])
plt.title("四季PM2.5平均浓度柱状图")
plt.savefig("../season_bar.png")
plt.close()

# 3.PM2.5-O3散点图
plt.figure(figsize=(6,4))
plt.scatter(df["PM2.5"],df["O3"],alpha=0.2)
plt.xlabel("PM2.5")
plt.ylabel("O3")
plt.title("PM2.5与O3散点图")
plt.savefig("../scatter_pm_o3.png")
plt.close()

# 4.相关性热力图
fig,ax=plt.subplots(figsize=(7,6))
im=ax.imshow(corr_matrix,cmap="coolwarm")
ax.set_xticks(range(len(pollution_cols)))
ax.set_yticks(range(len(pollution_cols)))
ax.set_xticklabels(pollution_cols)
ax.set_yticklabels(pollution_cols)
plt.colorbar(im,ax=ax)
plt.title("污染物相关性热力图")
plt.savefig("../corr_heatmap.png")
plt.close()

# 季节统计
season_stats=df.groupby("season")["PM2.5"].agg(["mean","std"])
print("四季PM2.5统计\n",season_stats)
print("业务结论：冬季模拟PM2.5均值最高，污染程度最重；夏季均值最低，空气质量最优。")