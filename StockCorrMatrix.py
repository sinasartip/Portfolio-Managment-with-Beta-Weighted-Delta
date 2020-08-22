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

def StockCorrelationMatrix(dir, plot = True):
    #create an array of stock names and stock pct
    dir = sorted_alphanumeric(os.listdir(dir))

    data = []
    headers = []
    try:    
        for index,file in enumerate(dir):
            headers.append(file[:-4])
            Stock = pd.read_csv(f"./correlation/{file}")
            Stock['pct'] = Stock['Close'].pct_change()
            data.append(Stock['pct'])
        pct_frame = pd.concat(data, axis=1, keys = headers)
        pct_frame = pct_frame.iloc[1:,] #delete the first the row (NaN)
            

        #heat map and correlation

        corr_frame = pct_frame.corr()
        corr_sorted = corr_frame.abs()
        
        #corr_sorted = corr_sorted.where(np.tril(np.ones(corr_sorted.shape),k=-1).astype(np.bool)).stack().sort_values(ascending=False)
        #print(corr_sorted)

        if plot == True:
            #setup figure
            fig, ax = plt.subplots(1,2)
            
            # Create a mask to hide upper part of the correlation matrix
            mask = np.triu(np.ones_like(corr_frame, dtype=np.bool))
            seaborn.heatmap(corr_frame, cmap='YlGnBu', mask=mask,ax = ax[0])
            seaborn.heatmap(corr_frame[corr_frame>=0.6], cmap='YlGnBu', mask=mask,ax = ax[1])
            
            plt.show()
    except Exception as error:
        print(error)
        print("There is likely a non csv file type in the folder")

if __name__ == "__main__":
   dir = "./correlation"
   StockCorrelationMatrix(dir)
   #You need to output array of stock with correlation above 0.6, there will be sets of stocks with this 
   #setup you should choose the largest
   