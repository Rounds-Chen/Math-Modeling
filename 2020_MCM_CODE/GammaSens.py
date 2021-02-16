# -------------------------------------------------------
# draw gamma distribution probability density curve
# -------------------------------------------------------


import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


# format the figure
def FormatFig(plt):
    # set axes format
    ax = plt.gca()
    plt.xlabel('Radius/km')  # set xlabel
    plt.ylabel('Probability Density')  # set ylabel
    ax.spines['top'].set_visible(False)  # close top-axis
    ax.spines['right'].set_visible(False)  # closr right-axis

    plt.axvline(x=5, linestyle='-.', lw=1, color='#FFD700')  # draw straight line perpendicular to the x-axis at x=5

    # set axes ticks format
    plt.tick_params(axis='x',
                    which='both',
                    labelsize=10,
                    labelcolor='#4d4f53',
                    )
    plt.tick_params(axis='y',
                    which='both',
                    pad=10,  # 刻度值与坐标轴框线的距离
                    labelsize=10,
                    labelcolor='#4d4f53',
                    )

    plt.legend(loc='best', prop={'size': 7})  # set legend format


# shapes,scales=[2.25,2.375,2.5,2.625,2.75],[3.731,3.84,3.951,4.031,4.145]
shapes, scales = [1.0, 1.005, 1.012, 0.99, 0.98], [0.5, 0.65, 0.7, 0.46, 0.52]
color = ['#6495ED', '#48D1CC', '#87CEFA', '#ADFF2F', '#FF8C00']
n = 10
out_value= []  # probability out special value
shape, scale = shapes[0], scales[0]
for shape, scale, c in zip(shapes, scales, color):
    x = np.random.gamma(shape, scale, n) # get n gamma distribution results
    sns.kdeplot(x, legend=True, label='shape=' + str(shape) + ' ' + 'scale=' + str(scale),
                color=c)  # draw probability density curve
    out_value.append(np.sum(x > 5) / len(x))

FormatFig(plt)
print(out_value)
plt.show()
