import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


##1.导入数据
plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False#显示中文
data=pd.read_csv('albums.csv')


##2.清洗数据
#数据基本信息
print('基本信息')
print(data.info(),'\n')
print('数据描述','\n',data.describe(),'\n')

#删除缺失值和重复值
data=data.dropna()
data=data.drop_duplicates()

#年份规整
data["year_of_pub"]=data["year_of_pub"].astype(int)

#1) album_title：音乐专辑名称
#2) genre：专辑类型
#3) year_of_pub： 专辑发行年份
#4) num_of_tracks： 每张专辑中单曲数量
#5) num_of_sales：专辑销量
#6) rolling_stone_critic：滚石网站的评分
#7) mtv_critic：全球最大音乐电视网MTV的评分
#8) music_maniac_critic：音乐达人的评分


##3.数据分析

#3.1统计各类专辑数量
g1=data.groupby("genre") #按genre分组
genre_numb=g1.size()  #逐行统计即为专辑数
genre_numb=genre_numb.sort_values(ascending=False)#降序排列
print('统计各类专辑数量')
print(genre_numb,'\n')

#3.2统计各类型专辑的销量总数
g2=data.groupby("genre")
sales=g2['num_of_sales'].sum()
sales=sales.sort_values(ascending=False)
print('统计各类型专辑的销量总数')
print(sales,'\n')

#3.3统计近20年每年发行的专辑数量和单曲数量
last_year=data["year_of_pub"].max()
start_year=last_year-19  #统计的是数据里面最后20年的数据而非今年
data_20=data[data["year_of_pub"]>=start_year]
g3=data_20.groupby("year_of_pub")  #按年份分组
album_numb=g3.size()  #每年专辑数量
track_numb=g3['num_of_tracks'].sum()  #每年单曲数量
print('统计近20年每年发行的专辑数量和单曲数量')
print(album_numb,'\n')
print(track_numb,'\n')

#3.4分析总销量前五的专辑类型的各年份销量
top5=sales.head(5)
top5_genre=top5.index  #索引
top5_data=data[data['genre'].isin(top5_genre)]  #保留前五数据
g4=top5_data.groupby(["year_of_pub","genre"])   #按年份和专辑分组
top5_year_sales=g4['num_of_sales'].sum()
print('统计近20年每年发行的专辑数量和单曲数量(仅展示首尾)')
print(top5_year_sales,'\n')

#3.5分析总销量前五的专辑类型，在不同评分体系中的平均评分
g5=top5_data.groupby("genre")
score=g5[["rolling_stone_critic","mtv_critic","music_maniac_critic"]].mean()  #分别的平均值
score["avg_score"]=score.mean(axis=1)  #每行平均值
score=score.sort_values("avg_score", ascending=False)
print(score)


##4.可视化图表分析
#4.1各类专辑数量柱状图
plt.figure(figsize=(10,5))
genre_numb.plot(kind="bar")  #柱状图
plt.title('各类型专辑数量统计')
plt.xlabel('音乐类型')
plt.ylabel('专辑数量')
plt.xticks(rotation=45)  #底下文字的倾斜角度
plt.show()

#4.2各类型专辑的销量总数柱状图(1e9=10⁹)
plt.figure(figsize=(10,5))
sales.plot(kind="bar")
plt.title('各类型专辑销量总数统计')
plt.xlabel('音乐类型')
plt.ylabel('销量总数')
plt.xticks(rotation=45)
plt.show()

#4.3近20年每年发行的专辑数量和单曲数量折线图
plt.figure(figsize=(10,5))
album_numb.plot(kind="line",marker="o",label="专辑数量")
track_numb.plot(kind="line",marker="^",label="单曲数量")
plt.title('近20年每年发行的专辑数量和单曲数量统计')
plt.xlabel('年份')
plt.ylabel('数量')
plt.xticks(album_numb.index,rotation=45)  #显示每一年，并改变文字倾角
plt.legend() #线条注释
plt.grid()  #显示网格
plt.show()

#4.4总销量前五的专辑类型的各年份销量
top5_year_sales=top5_year_sales.unstack()  #数据转换：将top5里的分类出来
plt.figure(figsize=(10,5))
top5_year_sales.plot(kind="line",marker="o")
plt.title("总销量前五的专辑类型的各年份销量")
plt.xlabel("年份")
plt.ylabel("销量")
plt.xticks(top5_year_sales.index,rotation=45)
plt.legend(title="音乐类型")
plt.grid()
plt.show()

#4.5总销量前五的专辑类型，在不同评分体系中的平均评分
score.plot(kind="bar",figsize=(10,5))
plt.title("总销量前五专辑类型不同评分体系平均评分")
plt.xlabel("专辑类型")
plt.ylabel("平均评分")
plt.legend(title="评分体系")
plt.grid(axis="y")
plt.show()
