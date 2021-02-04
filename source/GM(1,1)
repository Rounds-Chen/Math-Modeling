import numpy as np
import pandas as pd

data=[71.1,72.4,72.4,72.1,71.4,72.0,71.6] # 数据来源
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

# 输出预测数据
for i in range(len):
    print(data_prd[i])
