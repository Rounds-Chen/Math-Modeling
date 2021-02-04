import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# 绘图
##yvals为预测值，kind为拟合类型
def Draw(x,y,yvals,kind):
    plot1=plt.plot(x,y,'s',label='original values')
    plot2=plt.plot(x,yvals,'r',label=kind+'values')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend(loc=4)
    plt.title(kind)
    plt.show()

# 多项式拟合
## deg为多项式阶数
def PolyFit(x,y,deg):
    z=np.polyfit(x,y,deg)
    p=np.poly1d(z) # 获得拟合函数的多项式系数，按照阶数从高到低排列
    print("你和的多项式为：",p) # 显示拟合的多项式函数

    yvals=p(x) # 求对应于x的拟合多项式值
    # yvals=np.polyval(z,x) # 同上
    Draw(x,y,yvals,'polyfitting')



# curve_fit拟合
def Func(x,a,b): # 拟合函数形式,p为系数
    # a,b=p[0],p[1]
    return a*np.e**(b*x)

def CurveFit(x,y,Func):
    # 进行拟合
    popt,pcov=curve_fit(Func,x,y) # popt是拟合系数，pcov是在popt参数下得到的协方差
    yvals=Func(x,popt[0],popt[1])
    Draw(x, y, yvals, 'curvefitting')



x=[1,2,3,4,5,6,7,8] # 待拟合的节点数据
y=[15.3,20.5,27.4,36.6,49.1,65.6,87.87,117.6]
x,y=np.array(x),np.array(y)
CurveFit(x,y,Func)

