import numpy as np
import pandas as pd

pd.set_option('display.max_columns',None)
pd.set_option('display.float_format',lambda x:f"{x:.2f}")

orders=pd.DataFrame({
    "order_id":[f"O{number}" for number in range(1001,1019)],
    "region":["华东","华北","华南","华东","西南","华北","华南","华东","西南","华北","华东","华南","西南","华东","华北","华东","华北","华南"],
    "product":["机械键盘","无线鼠标","显示器","扩展坞","机械键盘","显示器","无线鼠标","显示器","扩展坞","机械键盘","显示器","无线鼠标","显示器","扩展坞","机械键盘","无线鼠标","扩展坞","显示器"],
    "category":["外设","外设","显示设备","配件","外设","显示设备","外设","显示设备","配件","外设","外设","配件","显示设备","外设","显示设备","配件","外设","外设"],
    "quantity":[2,3,1,4,5,2,6,1,3,2,8,2,1,3,5,2,4,6],
    "unit_price":[289,129,1299,399,289,1299,129,1299,399,289,129,399,1299,289,399,1299,129,289],
    "member_level":["金卡","普通","银卡","金卡","银卡","普通","金卡","银卡","普通","金卡","银卡","金卡","普通","银卡","金卡","金卡","普通","银卡"],
    "coupon_rate":[0.05,0.00,0.08,0.10,0.05,0.00,0.12,0.05,0.00,0.08,0.10,0.05,0.00,0.12,0.05,0.08,0.00,0.10],
    "salesperson":["小林","小周","小陈","小林","小赵","小周","小陈","小林","小赵","小周","小林","小陈","小赵","小周","小陈","小林","小赵","小周"]
})

#任务1:快速理解数据
#1.输出行数、列数、所有列名
print("1-1行数与列数:",orders.shape)
print("1-2列名:",orders.columns.tolist())

#2.取出region单列；order_id,product,quantity三列；打印类型
s_region=orders["region"]
df_cols=orders[["order_id","product","quantity"]]
print("region列类型:",type(s_region))
print("多列类型:",type(df_cols))

#3.iloc取第4‑8行(索引3‑7)，前4列
df_iloc=orders.iloc[3:8,:4]
print("1-3\n",df_iloc)

#4.loc筛选华东订单，展示order_id,product,member_level
df_east=orders.loc[orders["region"]=="华东",["order_id","product","member_level"]]
print("1-4\n",df_east)

#5.问题回答
answer_loc="loc基于标签名进行筛选，代码可读性更高；当表格行列发生变动时，iloc按数字索引容易取错数据，loc稳定性更强，适合长期业务维护。"
print("1-5:",answer_loc)

#任务2:构造订单结算指标，生成新表analysis
analysis=orders.copy()
#新增gross_amount:原始总价
analysis=analysis.assign(gross_amount=lambda df:df["quantity"]*df["unit_price"])
#member_discount:金卡0.1，银卡0.05，普通0，使用np.where嵌套
analysis["member_discount"]=np.where(analysis["member_level"]=="金卡",0.10,
                            np.where(analysis["member_level"]=="银卡",0.05,0.00))
#payable_amount:会员折扣+优惠券扣减后金额
analysis=analysis.assign(payable_amount=lambda df:df["gross_amount"]*(1-df["member_discount"])*(1-df["coupon_rate"]))
#shipping_fee:payable_amount>=1000运费0，否则20
analysis["shipping_fee"]=np.where(analysis["payable_amount"]>=1000,0,20)
#final_amount:最终金额
analysis=analysis.assign(final_amount=lambda df:df["payable_amount"]+df["shipping_fee"])
#保留两位小数
analysis=analysis.round(2)
print("任务2前8行:\n",analysis[["gross_amount","member_discount","payable_amount","shipping_fee","final_amount"]].head(8))

#任务3:复杂条件筛选
#条件1：地区为华东或华南
cond1=(analysis["region"]=="华东")|(analysis["region"]=="华南")
#条件2：final_amount>=500
cond2=analysis["final_amount"]>=500
#条件3：数量不少于2 或者会员为金卡
cond3=(analysis["quantity"]>=2)|(analysis["member_level"]=="金卡")
#组合mask
mask=cond1&cond2&cond3
df_focus=analysis.loc[mask,["order_id","region","product","quantity","member_level","final_amount"]]
#按金额降序
df_focus=df_focus.sort_values("final_amount",ascending=False)
print("任务3重点跟进订单:\n",df_focus)
#解释括号：位运算符&、|优先级高于比较运算符(>=,==)，不加括号会优先执行位运算，造成逻辑判断错误，必须对每个布尔条件加括号。

#任务4:封装函数新增订单等级，使用np.where嵌套
def add_order_level(df):
    df_new=df.copy()
    df_new["order_level"]=np.where(df_new["final_amount"]>=2000,"战略订单",
                          np.where(df_new["final_amount"]>=1000,"重点订单","普通订单"))
    return df_new
leveled_orders=analysis.pipe(add_order_level)
print("任务4各级订单数量:\n",leveled_orders["order_level"].value_counts())

#任务5:一条方法链完成经营汇总
region_report=(analysis
    .pipe(add_order_level)
    .query("final_amount>=500")
    .groupby(["region","order_level"])
    .agg(order_count=("order_id","count"),
         quantity_sum=("quantity","sum"),
         revenue_sum=("final_amount","sum"),
         revenue_mean=("final_amount","mean"))
    .sort_values("revenue_sum",ascending=False))
print("任务5经营汇总:\n",region_report)

#任务6:经营诊断
#1.找出成交总额最高的销售人员
sales_total=leveled_orders.groupby("salesperson")["final_amount"].sum()
top_sales=sales_total.idxmax()
top_total=sales_total.max()
#2.该销售人员各个地区成交金额
sales_region=leveled_orders[leveled_orders["salesperson"]==top_sales].groupby("region")["final_amount"].sum()
top_region=sales_region.idxmax()
region_value=sales_region.max()
#3.计算该地区占此人总金额比例
ratio=region_value/top_total
print(f"销售冠军:{top_sales},总成交金额:{top_total:.2f}")
print(f"核心地区:{top_region},核心地区金额:{region_value:.2f},占比:{ratio:.2%}")
print("业务结论：小林总销售额最高，其营收主要来自华东地区，华东贡献了他大部分的业绩，可加大该区域运营投入。")