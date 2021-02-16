import numpy as np
import pandas as pd

predata=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, '0.0', '2.4402962676997313', '5.151623965111442', '1.5003966271009868', '1.5003966271009868', '1.5003966271009868', '1.5003966271009868', '1.5003966271009868', '7.692234409096214', '24.55698050148976', '24.55698050148976', '7.483848516989283', '4.252811144437729', '4.031531128961622', '4.031531128961622', '4.031531128961622']
#['2019/01', '2019/02', '2019/03', '2019/04', '2019/05', '2019/06', '2019/07', '2019/08', '2019/09', '2019/10', '2019/11', '2019/12', '2020/01', '2020/02', '2020/03', '2020/04', '2020/05', '2020/06', '2020/07', '2020/08', '2020/09', '2020/10', '2020/11', '2020/12']
data=[]
for d in predata:
    d=float(d)
    if d==0:
        d=0.0000001
    data.append(d)


len=len(data) # 数据量

# 数据检验
lambdas=[]
for i in range(1,len):
    lambdas.append(data[i-1]/data[i])

X_Min=np.e**(-2/(len+1))
X_Max=np.e**(2/(len+1))

l_min,l_max=min(lambdas),max(lambdas)
if l_min<X_Min or l_max> X_Max:
    print("该组数据为通过数据检验，不能建立GM模型！")
else:
    print("改组数据通过检验")

# 建立GM(1,1)模型
data_1=[] # 累加数列
z_1=[]
data_1.append(data[0])
for i in range(1,len):
    data_1.append(data[i]+data_1[i-1])
    z_1.append(-0.5*(data_1[i]+data_1[i-1]))


B=np.array(z_1).reshape(len-1,1)
one=np.ones(len-1)
B=np.c_[B,one]
Y=np.array(data[1:]).reshape(len-1,1)
a,b=np.dot(np.dot(np.linalg.inv(np.dot(B.T,B)),B.T),Y)
print('a='+str(a))
print('b='+str(b))

## 数据预测
data_1_prd=[]
data_1_prd.append(data[0])
data_prd=[] # 预测data
data_prd.append(data[0])
for i in range(1,len):
    data_1_prd.append((data[0]-b/a)*np.e**(-a*i)+b/a)
    data_prd.append(data_1_prd[i]-data_1_prd[i-1])

# 模型检验
## 残差检验
e=[]
for i in range(len):
    e.append((data[i]-data_prd[i])/data[i])
e_max=max(e)
if e_max<0.1:
    print("数据预测达到较高要求！")
elif e_max<0.2:
    print("数据预测达到一般要求！")


