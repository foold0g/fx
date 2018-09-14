import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt

data = pd.read_csv("audusd.txt", sep=None, delimiter="\t", usecols=[0, 1], header=None)
np_data = np.array(data)
np_dates = [dt.datetime.strptime(x, '%d-%b-%Y').date() for x in np_data[:,0]]
plt.plot(np_dates, np_data[:,1])