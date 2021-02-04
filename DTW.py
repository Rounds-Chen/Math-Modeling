# Measuring time series similarity
# availabel at https://github.com/wannesm/dtaidistance
from dtaidistance import dtw
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

series=[
    np.array([0, 0, 1, 2, 1, 0, 1, 0, 0], dtype=np.double),
    np.array([0.0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0]),
    np.array([0.0, 0, 1, 2, 1, 0, 0, 0])
]

ds = dtw.distance_matrix_fast(series)
print(ds)
# Make a heat map
p1=sns.heatmap(ds,annot=True,linewidths=2,linecolor='white',cbar=True,cmap='PuBu')
p1.set_xticklabels([]) # x-axis value
p1.set_yticklabels([]) # y-axis value
p1.set_xlabel(' ')# xlabel
p1.set_ylabel(' ') # ylabel
p1.set_title(' ') # heatmap title
plt.show()
