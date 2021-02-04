"""
Autoregressive model for forecasting time series
ref:https://blog.csdn.net/htuhxf/article/details/105382451

"""
import warnings
from statsmodels.tsa.ar_model import AR
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error as MSE

warnings.filterwarnings('ignore', 'statsmodels.tsa.ar_model.AR', FutureWarning)

file_path=r" "# file path
df=pd.read_csv(file_path,index_col=0)

test_num=1 # test sets number
train,test=df.value[:-test_num], df.value[-test_num:]

#train AR model
model_fit=AR(train).fit()
params=model_fit.params
p=model_fit.k_ar # number of lags

history=train[-p:]
history=np.hstack(history).tolist()
test=np.hstack(test).tolist()

# validation test sets
preds=[]
for i in range(len(test)):
    lags=history[-p:]
    yhat=params[0]
    for t in range(p):
        yhat+=params[t+1]*lags[p-1-t]
    preds.append(yhat)
    history.append(test[t])

# show
plt.plot(test)
plt.plot(preds,color='r')
plt.show()
print(MSE(test,preds)**(0.5)) # RMSE
