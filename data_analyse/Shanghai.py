import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm
from statsmodels.tsa.api import Holt
from statsmodels.tsa.api import ExponentialSmoothing

sh=pd.read_csv('Shanghai (securities) composite index data.csv')
print(sh)