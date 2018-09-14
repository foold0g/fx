import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("audusd.txt", sep=None, delimiter="\t", usecols=[0, 1], header=None)
np_data = np.array(data)
plt.plot(np_data[:,0], np_data[:,1])