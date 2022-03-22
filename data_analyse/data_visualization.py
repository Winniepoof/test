import  pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm
from statsmodels.tsa.api import Holt
from statsmodels.tsa.api import ExponentialSmoothing

df=pd.read_csv('jetrail.csv',nrows=11858)

train=df[0:10392]
test=df[10392:]
train1=df[8929:10392]

df['Timestamp']=pd.to_datetime(df['Datetime'],format='%d-%m-%Y %H:%M') # 4位年用Y，2位年用y
df.index=df['Timestamp']
df=df.resample('D').mean()

train['Timestamp']=pd.to_datetime(train['Datetime'],format='%d-%m-%Y %H:%M')
train.index=train['Timestamp']
train = train.resample('D').mean()

train1['Timestamp']=pd.to_datetime(train1['Datetime'],format='%d-%m-%Y %H:%M')
train1.index=train1['Timestamp']
train1 = train1.resample('D').mean()

test['Timestamp'] = pd.to_datetime(test['Datetime'], format='%d-%m-%Y %H:%M')
test.index = test['Timestamp']
test=test.resample('D').mean()

train.Count.plot(figsize=(15,8),title= 'Daily Ridership', fontsize=14)
test.Count.plot(figsize=(15,8), title= 'Daily Ridership', fontsize=14)

#朴素法
# dd = np.asarray(train['Count'])
# y_hat = test.copy()
# y_hat['naive'] = dd[len(dd) - 1]
# plt.figure(figsize=(12, 8))
# plt.plot(train.index, train['Count'], label='Train')
# plt.plot(test.index, test['Count'], label='Test')
# plt.plot(y_hat.index, y_hat['naive'], label='Naive Forecast')
# plt.legend(loc='best')
# plt.title("Naive Forecast")
# plt.show()


#简单平均法
# y_hat_avg = test.copy()
#
# print(train)
# print(train1)
#
# y_hat_avg['avg_forecast'] = train1['Count'].mean()
# print(y_hat_avg)
# plt.figure(figsize=(12,8))
# plt.plot(train['Count'], label='Train')
# plt.plot(test['Count'], label='Test')
# plt.plot(y_hat_avg['avg_forecast'], label='Average Forecast')
# plt.legend(loc='best')
# plt.show()

#霍尔特线性趋势法

# sm.tsa.seasonal_decompose(train['Count']).plot()
# result = sm.tsa.stattools.adfuller(train['Count'])
# plt.show()
#
# y_hat_avg = test.copy()
#
# fit = Holt(np.asarray(train['Count'])).fit(smoothing_level=0.3, smoothing_slope=0.1)
# y_hat_avg['Holt_linear'] = fit.forecast(len(test))
#
# plt.figure(figsize=(16, 8))
# plt.plot(train['Count'], label='Train')
# plt.plot(test['Count'], label='Test')
# plt.plot(y_hat_avg['Holt_linear'], label='Holt_linear')
# plt.legend(loc='best')
# plt.show()

#Holt-Winters季节性预测模型
# y_hat_avg = test.copy()
# fit1 = ExponentialSmoothing(np.asarray(train['Count']), seasonal_periods=7, trend='add', seasonal='add', ).fit()
# y_hat_avg['Holt_Winter'] = fit1.forecast(len(test))
# plt.figure(figsize=(16, 8))
# plt.plot(train['Count'], label='Train')
# plt.plot(test['Count'], label='Test')
# plt.plot(y_hat_avg['Holt_Winter'], label='Holt_Winter')
# plt.legend(loc='best')
# plt.show()

#自回归移动平均模型
y_hat_avg = test.copy()
fit1 = sm.tsa.statespace.SARIMAX(train.Count, order=(2, 1, 4), seasonal_order=(0, 1, 1, 7)).fit()
y_hat_avg['SARIMA'] = fit1.predict(start="2013-11-1", end="2013-12-31", dynamic=True)
plt.figure(figsize=(16, 8))
plt.plot(train['Count'], label='Train')
plt.plot(test['Count'], label='Test')
plt.plot(y_hat_avg['SARIMA'], label='SARIMA')
plt.legend(loc='best')
plt.show()