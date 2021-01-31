import numpy as np

data=[4.93,2.33,3.87,4.35,6.63,7.15,5.37,6.39,7.81,8.35] # 原始数据
len=len(data)

data_1=[] # 累加数列
z_1=[]
data_1.append(data[0])
for i in range(1,len):
    data_1.append(data[i]+data_1[i-1])
    z_1.append(-0.5*(data_1[i]+data_1[i-1]))

B=np.array(z_1).reshape(len-1,1)
B_=B**2
B=np.c_[B,B_]
Y=np.array(data[1:]).reshape(len-1,1)
a,b=np.dot(np.dot(np.linalg.inv(np.dot(B.T,B)),B.T),Y)
print('a='+str(a))
print('b='+str(b))

data_1_prd=[]
data_1_prd.append(data[0])
data_prd=[] # 预测data
data_prd.append(data[0])
for i in range(1,len):
    data_1_prd.append(a*data[0]/(b*data[0]+(a-b*data[0])*np.e**(a*i)))
    data_prd.append(data_1_prd[i]-data_1_prd[i-1])

## 数据预测值
for i in range(len):
    print(data_prd[i])

## 预测值误差
e=[]
for i in range(len):
    e.append(100*(data[i]-data_prd[i])/data[i])
    print(e[i])