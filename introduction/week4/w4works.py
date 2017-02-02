import pandas as pd
import numpy as np
import scipy.stats as stats

# print (np.random.binomial(10, 0.5, 5))

# print (np.random.binomial(1000, 0.5)/1000)

# COT = 0.01
# tornado_events = np.random.binomial(1, COT, 1000000)
# two_days_in_a_row = 0
# for j in range(1, len(tornado_events)-1):
# 	if tornado_events[j]==1 and tornado_events[j-1]==1:
# 		two_days_in_a_row += 1
# print('{} tornadoes back to back in {} years' .format(two_days_in_a_row, 1000000/365))

# print (np.random.uniform(0, 1))

# print(np.random.normal(0.75))

distribution = np.random.normal(0.75, size=1000)
# print(np.sqrt(np.sum((np.mean(distribution)-distribution)**2)/len(distribution)))
# print(np.std(distribution))
# print(stats.kurtosis(distribution))
# print(stats.skew(distribution))

chi_squared_df2 = np.random.chisquare(2, size=10000)
# print(stats.skew(chi_squared_df2))

chi_squared_df5 = np.random.chisquare(5, size=10000)
# print(stats.skew(chi_squared_df5))

# from IPython import get_ipython
# ipython = get_ipython()
# import matplotlib
# import matplotlib.pyplot as plt
# ipython.magic('matplotlib inline')
# output = plt.hist([chi_squared_df2, chi_squared_df5], bins=50, histtype='step', label=['2 degrees of freedom', '5 degrees of freedom'])
# plt.legend(loc='upper right')
