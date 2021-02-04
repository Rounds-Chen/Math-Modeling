from sklearn.datasets import make_blobs
from sklearn.neighbors import KNeighborsClassifier
import  numpy as np
import matplotlib.pyplot as plt


# 绘制分类图形
# X为样本数据集，Y为标签集，knn为KNN模型
def Draw(X,Y,knn):
    x_min,x_max=min(X[:,0])-1,max(X[:,0])+1
    y_min,y_max=min(X[:,1])-1,max(X[:,1])+1

    xx,yy=np.meshgrid(np.arange(x_min,x_max,.02),np.arange(y_min,y_max,.02)) # 横纵网格点
    #xx,yy=np.meshgrid(np.linspace(x_min,x_max,num=20),np.linspace(y_min,y_max,num=1000))
    z=knn.predict(np.c_[xx.ravel(),yy.ravel()]) # 网格交叉点
    z=z.reshape(xx.shape)

    plt.pcolormesh(xx,yy,z,cmap=plt.cm.get_cmap('Pastel2'))
    plt.scatter(X[:,0],X[:,1],c=Y,cmap=plt.cm.get_cmap('spring'), edgecolors='k')
    plt.xlim(xx.min(),xx.max())
    plt.ylim(yy.min(),yy.max())
    plt.show()

# 产生的模拟数据
X,Y=make_blobs(n_samples=200,n_features=2,centers=5,cluster_std=1.0,random_state=8)

knn=KNeighborsClassifier()
knn.fit(X,Y) # X为数据集，Y为各数据对应的标签

Draw(X,Y,knn)