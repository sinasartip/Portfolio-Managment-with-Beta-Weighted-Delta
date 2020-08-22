#%%
import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np
from scipy.stats import linregress
import seaborn
import os


def sorted_alphanumeric(data):
    import re
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(data, key=alphanum_key)

def dfsize(dir):
    sizes = np.zeros([np.shape(dir)[0],])
    for index, file in enumerate(dir):
        df = pd.read_csv(file)
        sizes[index] = df.shape[0]
    
    return sizes.max(axis=0)

#%%
#create an array of stock names and stock pct
dir = "./correlation"
dir = sorted_alphanumeric(os.listdir(dir))

data = []
headers = []

for index,file in enumerate(dir):
    headers.append(file[:-4])
    Stock = pd.read_csv(f"./correlation/{file}")
    Stock['pct'] = Stock['Close'].pct_change()
    data.append(Stock['pct'])
pct_frame = pd.concat(data, axis=1, keys = headers)
pct_frame = pct_frame.iloc[1:,] #delete the first the row (NaN)
    
# %%
#heat map and correlation

corr_frame = pct_frame.corr()

#setup figure
fig, ax = plt.subplots()

#  Create a mask to hide upper part of the correlation matrix
mask = np.triu(np.ones_like(corr_frame, dtype=np.bool))
seaborn.heatmap(corr_frame, cmap='YlGnBu', mask=mask)
plt.show()
# %%
