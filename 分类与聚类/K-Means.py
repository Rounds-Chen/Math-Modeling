from sklearn.cluster import KMeans,MiniBatchKMeans
from sklearn.datasets import make_blobs # 产生样本数据
import matplotlib.pyplot as plt


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
def draw(X,f):
    ctrs=f.cluster_centers_
    Y=f.predict(X)

    # 呈现归集后的数据
    plt.scatter(X[:, 0], X[:, 1], c=Y)
    plt.scatter(ctrs[:, 0], ctrs[:, 1], c='red')
    plt.show()


k=5 # 簇数
X,y=make_blobs(n_samples=1000,centers=k,random_state=1) # 样本点产生

km=kmeans(k,X)
draw(X,km)