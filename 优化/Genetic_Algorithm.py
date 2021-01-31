import geatpy as ea
import numpy as np

class MyProblem(ea.Problem):
    def __init__(self):
        name="Problem_12.1" # 问题名称
        M=1 # 目标维度
        maxormins=[1] # 目标最小最大化标记，1：最小化该目标；-1：最大化该目标
        Dim=2 # 决策变量维度
        varTypes=[0]*Dim # 决策变量类型，0：连续性；1：离散型
        lb=[-100]*Dim # 决策变量下界
        ub=[100]*Dim # 决策变量上界
        lbin=[1]*Dim # 是否包括决策变量上界
        ubin=[1]*Dim # 是否包括决策变量下界
        # 调用父类构造方法完成实例化
        ea.Problem.__init__(self,name,M,maxormins,Dim,varTypes,lb,ub,lbin,ubin)

    def aimFunc(self,pop): # 目标函数
        x1=pop.Phen[:,[0]]
        x2=pop.Phen[:,[1]]
        f=(x1-2)**2+(x2-1)**2
        CV1=-x1+2*x2-1
        CV2=-x1*x1/4+x2*x2-1
        CV=np.hstack((CV1,CV2))
        pop.CV=CV # 约束矩阵(注意<=0表示满足，越大越不满足）
        pop.ObjV=f # 目标函数

# 实例化问题变量
problem=MyProblem()

'''----------------------种群设置--------------------------------------'''
Encoding='BG' # 编码方式，BG表示二进制/格雷编码
NIND=100 # 种群规模
Field=ea.crtfld(Encoding,problem.varTypes,problem.ranges,problem.borders) # 区域描述器
population=ea.Population(Encoding,Field,NIND) #生成初始种群


'''-----------------------算法模板调用------------------------------------'''
myAlgo=ea.soea_EGA_templet(problem,population)# 实例化算法模板对象
myAlgo.MAXGEN=200 # 最大进化代数
myAlgo.logTras=1 #每隔多少代记录日志，0表示不记录
myAlgo.verbose=True # 是否打印日志信息
myAlgo.drawing=1 # 绘图方式，1：绘制结果图 2：绘制目标空间过程动画 3：绘制决策空间过程动画


''''----------------------调用算法模板进行种群进化------------------------------'''
[BestIndi, population]=myAlgo.run()  # 执行算法模板，得到最优个体及最后一代种群
BestIndi.save() # 保存最优个体信息至文件

'''--------------------------输出结果----------------------------------------'''
print('用时：%f 秒' % myAlgo.passTime)
print('评价次数：%d 次' % myAlgo.evalsNum)
if BestIndi.sizes != 0:
    print('最优的目标函数值为：%s' % BestIndi.ObjV[0][0])
    print('最优的控制变量值为：')
    for i in range(BestIndi.Phen.shape[1]):
        print(BestIndi.Phen[0, i])
else:
    print("未找到可行解")