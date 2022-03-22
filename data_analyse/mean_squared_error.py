from sklearn.metrics import mean_squared_error
from math import sqrt
import  pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df=pd.read_csv('jetrail.csv',nrows=11858)

train=df[0:10392]
test=df[10392:]

dd = np.asarray(train['Count'])
y_hat = test.copy()
y_hat['naive'] = dd[len(dd) - 1]
# plt.figure(figsize=(12, 8))
# plt.plot(train.index, train['Count'], label='Train')
# plt.plot(test.index, test['Count'], label='Test')
# plt.plot(y_hat.index, y_hat['naive'], label='Naive Forecast')
# plt.legend(loc='best')
# plt.title("Naive Forecast")
# plt.show()


rms=sqrt(mean_squared_error(test['Count'],y_hat['naive']))
print(rms)