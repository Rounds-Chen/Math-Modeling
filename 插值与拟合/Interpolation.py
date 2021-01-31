from scipy.interpolate import interp1d,interp2d

# 一维插值
x=[] # 节点数据
y=[]

# kind可取nearest,zero,slinear,quadratic,cubic
## nearest,zero为阶梯插值
## slinear 为线性插值
## quadratic，cubic 为2阶，3阶样条曲线插值
kind='cubic'
f_1d=interp1d(x,y,kind=kind) # kind类的插值函数


# 二维插值
x,y=[],[] # 节点x-y
z=[] # 节点z

# kind同上
f_2d=interp2d(x,y,z,kind='cubic')