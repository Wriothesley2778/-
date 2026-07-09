import numpy as np


def create_arrays():
    print("1.创建不同维度的数组")

    arr_1d=np.array([1,2,3,4,5])
    print(f"1D数组:{arr_1d}")
    print(f"形状:{arr_1d.shape},维度:{arr_1d.ndim}, 类型:{arr_1d.dtype}")
    print()

    arr_2d=np.array([[1,2,3], [4,5,6], [7,8,9]])
    print(f"2D数组:\n{arr_2d}")
    print(f"形状:{arr_2d.shape},维度:{arr_2d.ndim}")
    print()

    arr_3d=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
    print(f"3D数组:\n{arr_3d}")
    print(f"形状:{arr_3d.shape}, 维度:{arr_3d.ndim}")
    print()

    zeros_arr=np.zeros((2, 3))
    print(f"全零数组:\n{zeros_arr}")

    ones_arr=np.ones((3, 3))
    print(f"\n全一数组:\n{ones_arr}")

    identity_arr=np.eye(3)
    print(f"\n单位矩阵:\n{identity_arr}")

    range_arr=np.arange(0,10,2)
    print(f"\n等差数列数组:{range_arr}")

    linspace_arr=np.linspace(0,1,5)
    print(f"线性间隔数组:{linspace_arr}")

    return arr_1d,arr_2d,arr_3d


def array_indexing_slicing(arr_1d,arr_2d,arr_3d):
    print()
    print("2.数组的索引与切片")

    print("   1D数组索引与切片")
    print(f"原始数组:{arr_1d}")
    print(f"索引[0]:{arr_1d[0]}")
    print(f"索引[-1]:{arr_1d[-1]}")
    print(f"切片[1:4]:{arr_1d[1:4]}")
    print(f"切片[::2]:{arr_1d[::2]}")
    print(f"反转数组:{arr_1d[::-1]}")
    print()

    print("    2D数组索引与切片")
    print(f"原始数组:\n{arr_2d}")
    print(f"索引[1,2]:{arr_2d[1,2]}")
    print(f"切片[0:2,1:]:\n{arr_2d[0:2,1:]}")
    print(f"获取第一列:{arr_2d[:,0]}")
    print(f"获取第二行:{arr_2d[1,:]}")
    print()

    print("    3D数组索引与切片")
    print(f"原始数组:\n{arr_3d}")
    print(f"索引[0,1,1]: {arr_3d[0,1,1]}")
    print(f"切片[0,:,:]:\n{arr_3d[0,:,:]}")
    print(f"切片[:,0,:]:\n{arr_3d[:,0,:]}")


def shape_transformations(arr_2d):
    print()
    print("3.形状变换操作")

    print(f"原始数组:\n{arr_2d}")
    print(f"原始形状:{arr_2d.shape}")

    reshaped=arr_2d.reshape(1,9)
    print(f"\nreshape(1,9):\n{reshaped}")

    flattened=arr_2d.flatten()
    print(f"\nflatten():{flattened}")

    raveled=arr_2d.ravel()
    print(f"\nravel():{raveled}")

    transposed=arr_2d.T
    print(f"\n转置(T):\n{transposed}")

    arr_2d.resize(9,1)
    print(f"\nresize(9,1)后:\n{arr_2d}")


def matrix_operations():
    print()
    print("4.矩阵基本运算")

    A=np.array([[1,2],[3,4]])
    B=np.array([[5,6],[7,8]])
    print(f"矩阵A:\n{A}")
    print(f"\n矩阵B:\n{B}")

    def matrix_addition(m1,m2):
        if m1.shape!=m2.shape:
            raise ValueError("两个矩阵的形状必须相同")
        return m1+m2

    def matrix_multiplication(m1,m2):
        if m1.shape[1]!=m2.shape[0]:
            raise ValueError("第一个矩阵的列数必须等于第二个矩阵的行数")
        rows_m1, cols_m1=m1.shape
        rows_m2, cols_m2=m2.shape
        result=np.zeros((rows_m1,cols_m2))
        for i in range(rows_m1):
            for j in range(cols_m2):
                for k in range(cols_m1):
                    result[i,j]+=m1[i,k]*m2[k,j]
        return result

    def matrix_transpose(m):
        rows,cols=m.shape
        result=np.zeros((cols,rows))
        for i in range(rows):
            for j in range(cols):
                result[j,i] = m[i,j]
        return result

    print(f"\n矩阵加法(A+B):\n{matrix_addition(A,B)}")
    print(f"\n矩阵乘法(A×B):\n{matrix_multiplication(A,B)}")
    print(f"\n矩阵A的转置:\n{matrix_transpose(A)}")

    print(f"\n验证:NumPy内置加法:\n{A+B}")
    print(f"\n验证:NumPy内置乘法:\n{A@B}")
    print(f"\n验证:NumPy内置转置:\n{A.T}")


def random_data_analysis():
    print()
    print("5.随机数据生成与统计分析")

    np.random.seed(42)

    normal_data=np.random.normal(0,1,1000)
    print(f"正态分布数据(均值=0,标准差=1,1000个样本)")
    print(f"前10个数据:{normal_data[:10]}")
    print(f"均值:{np.mean(normal_data):.4f}")
    print(f"中位数:{np.median(normal_data):.4f}")
    print(f"标准差:{np.std(normal_data):.4f}")
    print(f"方差:{np.var(normal_data):.4f}")
    print(f"最小值:{np.min(normal_data):.4f}")
    print(f"最大值:{np.max(normal_data):.4f}")
    print(f"25%分位数:{np.percentile(normal_data,25):.4f}")
    print(f"75%分位数:{np.percentile(normal_data,75):.4f}")
    print()

    uniform_data=np.random.uniform(0,1,500)
    print(f"均匀分布数据(范围=[0,1],500个样本)")
    print(f"均值:{np.mean(uniform_data):.4f}")
    print(f"标准差:{np.std(uniform_data):.4f}")
    print()

    randint_data=np.random.randint(1,100,200)
    print(f"整数随机数据(范围=[1,100],200个样本)")
    print(f"前20个数据:{randint_data[:20]}")
    print(f"唯一值数量:{len(np.unique(randint_data))}")
    print(f"出现次数最多的值:{np.bincount(randint_data).argmax()}")


if __name__=="__main__":
    arr_1d,arr_2d,arr_3d=create_arrays()
    array_indexing_slicing(arr_1d,arr_2d,arr_3d)
    shape_transformations(arr_2d)
    matrix_operations()
    random_data_analysis()

    print("所有NumPy基础操作演示完成!")