# KNN

KNN(K-Nearest Neighbor)最近邻算法是数据分类（classification）中最简单算法之一。

计算未知类别样本与所有已知类别样本的距离，选取距离最近的K个样本，将未知样本归为K个最近邻样本中占比最多的类别。

## 关键

1. 样本所有特征要能够比较量化；
2. 样本特征归一化处理；
3. 距离函数：欧氏距离，余弦距离，曼哈尔顿距离等；
4. K值选取：太大会过拟合，太小会欠拟合，需交叉验证确定；



## 特点

1. 适用于稀有事件的分类；
2. 适合多分类问题，比SVM（支持向量机）表现好；
3. 计算量大。



## 使用KNeighborsClassifier

```python
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
```

 **示例结果：**![Figure_1](C:%5CUsers%5Cround%5CDesktop%5CFigure_1.png)

### 参数解析

```python
sklearn.neighbors.KNeighborsClassifier(n_neighbors=5,weights=’uniform’,algorithm=’auto’,leaf_size=30,p=2,metric=’minkowski’,metric_params=None,n_jobs=1,*kwargs) 
```

[官方文档](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html)

* **n_neighbors**：K值，默认5
* **weights**：参与预测的权重，
  * `uniform`：权重统一
  * `distance`：权重为距离的倒数
  * `[callable]`：用户自定义，该方法接收一个距离数组，返回相同形状的权重数组
* **algorithm**：计算最近邻的算法，
  * `ball_tree`：[ball_tree](http://scikit-learn.org/stable/modules/generated/sklearn.neighbors.BallTree.html#sklearn.neighbors.BallTree)
  * `kd_tree`：[kd_tree](http://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KDTree.html#sklearn.neighbors.KDTree)
  * `brute`：基本的暴力knn算kd_tree法
  * `auto`：根据传入数据集自动选择合kd_tree适的算法
* **leaf_size**：默认30，ball_tree和kd_tree算法的叶子数量
* **p**：默认2，表示何种距离
  * 1：曼哈顿距离
  * 2：欧氏距离
* **metric_params**：描述其他关键词参数的矩阵
* **n_jobs**：默认值1，可并行运行的任务数量



### 参考：

https://blog.csdn.net/pengjunlee/article/details/82713047

https://www.cnblogs.com/qfwmy/archive/2019/12/27/12106725.html