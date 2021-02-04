# K-Means算法

分类与聚类的区别：分类的目标事先已知；聚类的目标事先未知。

聚类算法有许多，K-Means是最常用的一种。只适用于**连续型数据**，并且要聚类前**指定分成几类**。



## 基本思想

1. 输入分类的簇数k；
2. 选取k个点作为聚类的簇心；
3. 根据每个样本点到簇心的距离，找到各自距离最近的簇心，将其归属到该簇；
4. 重新计算每个簇的簇心（平均距离中心），将其定义为新的簇心；
5. 重复3~4步骤，直到终止条件。



### 思考

1. **K值选择**：没有确定的做法，需要先验知识；

2. **初始簇心的选择**：可以随机，但K-Means算法初值敏感，衍生了：二分K-Means算法，K-Means++算法，K-Means||算法，Canopy算法等；

3. **离群值处理**：远离整体的特殊数据点在聚类前要去掉，单独作为一类处理；

4. **选择新的簇心**：每簇样本各个维度的平均值。新的簇心可能不是一个实际的样本点。

5. **标准化**：样本各维度数据的单位要一致，距离的计算才能有参考价值；若单位不一致，且进行欧几里得距离计算时，要将数据进行标准化，去除单位的限制，转换为无量纲的纯数值。

   常用的标准化方法：

   1. min-max标准化：将原始数据转换到[0,1]区间内，$x^`=(x-min)/(max-min)$;
   2. z-score标准化：处理后数据符合标准正态分布，$x^`=(x-均值)/标准差$



### 距离计算方法

* **欧氏距离**

$$
d(x,y)=\sqrt{(x_1-y_1)^2+(x_2-y_2)^2+\cdots+(x_n-y_n)^2}
$$

* **余弦距离**

$$
cos(\theta)=\frac{A·B}{|A||B|}
$$

* **曼哈顿距离**

直角坐标系中，两点对应线段在x，y轴投影长度总和：
$$
d(x,y)=|x_1-x_2|+|y_1-y_2|
$$




## 基本代码

```python
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
```

### 示例：

![Figure_1](C:%5CUsers%5Cround%5CDesktop%5CFigure_1.png)

### KMeans参数

1. `n_clusters`: K值
2. `max_iter`: 最大迭代次数。收敛数据集（凸集）不用考虑，非收敛数据集要设置用来退出循环
3. `n_init`：用不同的初始簇心运行算法的次数。由于K-Means算法初值敏感，因此需要使用不同的初始簇心多运行几次。默认值10
4. `init`：初始簇心选择方法，默认优化过的'`k-means++`'，可以随机选择'`random`'
5. `algorithm`：‘`auto`’，‘`full`’，‘`elkan`’三种选择。‘`full`’是k-means算法，‘`elkan`’是elkan k-means算法。默认值’`auto`‘根据数据集稀疏程度决定使用’`full`‘（稠密）还是’`elkan`‘（稀疏）
6. `random_state`：随机数产生方法，默认None，使用`np.random.RandomState`实例



## 一些优化

### Mini Batch K-Means算法

K-Means算法的优化变种，采用小规模数据子集（随机抽取数据子集）减少计算时间，并试图优化目标函数。

Mini Batch K-Means算法可减少K-Means算法收敛时间，产生略差于K-Means算法的结果。

#### 代码

```python
# 构建min-batch-kmeans模型
# k为簇数，size为batch-size，X为数据集
def mbkmeans(k,size,X):
    mbkm=MiniBatchKMeans(n_clusters=k,batch_size=size)
    mbkm.fit(X)
    return mbkm

```



## 参考

https://blog.csdn.net/u013850277/article/details/88411966

https://blog.csdn.net/sinat_36710456/article/details/88019323

