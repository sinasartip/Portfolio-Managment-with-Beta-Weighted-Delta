
import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np
from scipy.stats import linregress
import seaborn
import os
import math

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
    dir = os.listdir(dir)

    data = []
    headers = []
       
    RawStockData = pd.read_csv(f"./correlation/data.csv")
    
    for stock in RawStockData.columns:
        if stock.endswith('3'):
            
            data.append(RawStockData.loc[1:,stock].astype(float).pct_change())
         
            headers.append(stock[:-4])


    pct_frame = pd.concat(data, axis=1, keys = headers)
    pct_frame = pct_frame.iloc[1:,] #delete the first the row (NaN)
        

    
    #count highest correlation stocks
    corr_frame = pct_frame.corr()
    #corr_sorted = corr_frame.abs() #to find corr regardless of +-
    corr_sorted = corr_frame
    #corr_sorted = corr_sorted.where(np.tril(np.ones(corr_sorted.shape),k=-1).astype(np.bool))
    #corr_sorted = corr_sorted[corr_sorted>=0.6]
    corr_sorted = corr_sorted[corr_sorted<=-0.6] #to find negative corr
    #print(corr_sorted)
    stockname = corr_sorted.columns
    highest_corr = pd.DataFrame(index = stockname, columns = ["NumOfRep"])
    
    for item in stockname:
        count = corr_sorted[item].notna().sum()
        highest_corr.loc[item,'NumOfRep'] = count
    print("--------")
    highest_corr = highest_corr.loc[:,'NumOfRep'].sort_values(ascending=False)
    #print(highest_corr)

    #heat map and correlation
    if plot == True:
        #setup figure
        fig, ax = plt.subplots()
        
        # Create a mask to hide upper part of the correlation matrix
        mask = np.triu(np.ones_like(corr_frame, dtype=np.bool))
        #seaborn.heatmap(corr_frame, cmap='YlGnBu', mask=mask,ax = ax[0])
        seaborn.heatmap(corr_frame[corr_frame<=-0.6], cmap='YlGnBu', mask=mask)
        
        plt.show()

    return [corr_sorted, highest_corr]
    #except Exception as error:
    #    print(error)
    #   print("There is likely a non csv file type in the folder")

if __name__ == "__main__":

    dir = "./correlation"
    corr_sorted, highest_corr = StockCorrelationMatrix(dir,plot=False)
    data = corr_sorted[corr_sorted['XIU.'].notna()]
    print(data['XIU.'])


