import numpy as np

name_list=[]
score_list=[]

def input_data():
    name_list.clear()
    score_list.clear()
    num=int(input("请输入学生人数:"))
    for i in range(num):
        name=input(f"请输入第{i+1}个学生姓名:")
        score=int(input("请输入成绩:"))
        name_list.append(name)
        score_list.append(score)
    print("数据录入完成")

def stat_info():
    if len(score_list)==0:
        print("暂无成绩数据，请先录入")
        return
    arr=np.array(score_list)
    print(f"总分:{arr.sum()}")
    print(f"平均分:{arr.mean():.2f}")
    print(f"最高分:{arr.max()}")
    print(f"最低分:{arr.min()}")

def sort_rank():
    if len(score_list)==0:
        print("暂无成绩数据，请先录入")
        return
    arr=np.array(score_list)
    idx=np.argsort(-arr)
    print("排名|姓名|成绩")
    for r,i in enumerate(idx):
        print(f"{r+1}|{name_list[i]}|{score_list[i]}")

def score_distribute():
    if len(score_list)==0:
        print("暂无成绩数据，请先录入")
        return
    arr=np.array(score_list)
    excellent=len(arr[arr>=90])
    good=len(arr[(arr>=80)&(arr<90)])
    mid=len(arr[(arr>=60)&(arr<80)])
    bad=len(arr[arr<60])
    print("成绩等级分布")
    print(f"90分以上(优秀):{excellent}人")
    print(f"80-89(良好):{good}人")
    print(f"60-79(及格):{mid}人")
    print(f"60以下(不及格):{bad}人")

def search_student():
    if len(name_list)==0:
        print("暂无成绩数据，请先录入")
        return
    target=input("输入要查询的学生姓名:")
    if target in name_list:
        pos=name_list.index(target)
        print(f"{target}成绩:{score_list[pos]}")
    else:
        print("未找到该学生")

def menu():
    while True:
        print("="*30)
        print("成绩分析系统")
        print("="*30)
        print("1.输入成绩数据")
        print("2.查看成绩统计")
        print("3.查看成绩排名")
        print("4.查看成绩分布")
        print("5.查询学生成绩")
        print("6.退出系统")
        choice=input("请选择:")
        if choice=="1":
            input_data()
        elif choice=="2":
            stat_info()
        elif choice=="3":
            sort_rank()
        elif choice=="4":
            score_distribute()
        elif choice=="5":
            search_student()
        elif choice=="6":
            print("程序退出")
            break
        else:
            print("输入错误，请重新选择")

if __name__=="__main__":
    menu()