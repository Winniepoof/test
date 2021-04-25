import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split, GridSearchCV

df = pd.read_csv('train.csv')
features_raw = df.drop('label', axis=1)
label = df['label']
print(df.duplicated().sum())
df.drop_duplicates(inplace=True)
X_train, X_test, y_train, y_test = train_test_split(features_raw, label, test_size=0.3, random_state=2021)
regr = GradientBoostingRegressor()

param_list = {
    'n_estimators': np.arange(10, 101, 10),
    'learning_rate': np.arange(0.1, 1, 0.1),
    'subsample': np.arange(0.5, 0.8, 0.1),
    'max_depth': np.arange(3, 100, 1),
}
grid = GridSearchCV(regr, param_grid=param_list, cv=5)

grid.fit(X_train, y_train)

print(grid.best_params_)
print(grid.best_score_)
print(grid.best_estimator_)
print(grid.best_index_)