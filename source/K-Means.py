from sklearn.cluster import KMeans,MiniBatchKMeans
from sklearn.datasets import make_blobs # 产生样本数据
import matplotlib.pyplot as plt
import csv
import numpy as np
from sklearn import preprocessing


# 构建K-Means模型
#k为簇数，X为数据集
def kmeans(k,X):
    km=KMeans(n_clusters=k)
    km.fit(X)
    return km

# 构建min-batch-kmeans模型
# k为簇数，size为batch-size，X为数据集
def mbkmeans(k,size,X):
    mbkm=MiniBatchKMeans(n_clusters=k,batch_size=size)
    mbkm.fit(X)
    return mbkm

#可视化
def draw(X,f,date):
    ctrs=f.cluster_centers_
    Y=f.predict(X)

    # 呈现归集后的数据
    plt.scatter(X[:, 0], X[:, 1], c=Y)
    plt.scatter(ctrs[:, 0], ctrs[:, 1],c='red')

    for i in range(0,X.shape[0]-1):
        print(X[i][0],X[i][1])
        plt.text(X[i][0],X[i][1],date[i])
    plt.show()

data=[]
f=open(r'C:\Users\round\PycharmProjects\AI\Math_Modeling\3.csv','r')
csv_reader=csv.reader(f)
for row in csv_reader:
    data.append(row)
data=data[1:]
data_n=[]
date=[]
for item in data:
    temp=[]
    for i in item[1:]:
        temp.append(float(i))
    date.append(item[0])
    #if temp[0]>100:
    data_n.append(temp)


data_n=np.array(data_n)
print(data_n)


#k=5 # 簇数
#X,y=make_blobs(n_samples=1000,centers=k,random_state=1) # 样本点产生


min_max_scaler = preprocessing.MinMaxScaler()
x_minmax = min_max_scaler.fit_transform(data_n)
#print(x_minmax)

k=3
km=kmeans(k,x_minmax)
ctrs=km.cluster_centers_
# print(ctrs)
draw(x_minmax,km,date)
