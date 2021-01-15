#%%
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
from scipy.stats import linregress
import os
from GrabStockData import grabData
#%matplotlib inline
def BetaWeightedOption(beta, StockPrice, ReferencePrice, OptionDelta):
    """To calculate the beta weighted delta on an option you can use the following formula:
        BetaWeightedDelta of Option = beta * $Underlying * Delta of Underlying / $reference

        using the output of this formula you can now add your options beta weighted delta to that of 
        the rest of your portfolio. 
    Input: 
        beta : beta of underlying 
        StockPrice : Current Price of underlying 
        ReferencePrice : Current Price of the stock you beta weighted the portfolio to 
        OptionDelta : The Delta value of the option you want to trade (belonging to the underlying you 
        provided.)
    """

    betaO = (beta * StockPrice * OptionDelta) / ReferencePrice 
    return betaO

def BetaWeightedDelta(dir, StockClose, ReferenceClose, plot = True): 
    """The beta weighted delta shows how many points your stock will move
    for any given move of the reference. 
    The beta weighting allows you to add the various deltas of your portfolio to 
    find a final whole portfolio delta, normalized to the reference. 
    
    Inputs : 
        StockName = Directory to you Stock (use the stock ticker as file name)
        ReferenceName = Directory to you Stock (use the stock ticker as file name)
        
        Use yahoo finance histric prices and place them all in the same folder. 
        The number of data points can be different, the function will adjust the sizes. 
        
        plot : If you want to see a plot of the percent price changes and the beta regression line 
               you also get the R^2 value for a wellness of fit. 
               
    Output : 
        Beta : beta weighting of your stocks  delta 
        R^2 : wellness of fit of the beta  """
    #Read in portfolio values & calculate the percent change 
    #Reference is the reference value


    StockList = pd.read_csv(f"{dir}/data.csv")
    
    Stock = StockList.loc[1:,StockClose].astype(float).pct_change()
    Stock=Stock.iloc[1:,] #delete the first the row (NaN)
    Reference = StockList.loc[1:,ReferenceClose].astype(float).pct_change()
    Reference=Reference.iloc[1:,] #delete the first the row (NaN)
 
    #The first element is NaN
    Stock_pct = Stock.to_numpy()
    Stock_pct = np.delete(Stock_pct, 0)
    Reference_pct = Reference.to_numpy()
    Reference_pct = np.delete(Reference_pct, 0)
    #print(f"Shape of reference: {Reference_pct.shape}")
    #print(f"Shape of Stock {Stock_pct.shape}")

    #adjust shape of input data if needed 
    if Reference_pct.shape != Stock_pct.shape:
        ShapeDiff = abs(Reference_pct.shape[0] - Stock_pct.shape[0])
        print(f"Shape Difference {ShapeDiff}")
        if Reference_pct.shape < Stock_pct.shape:
            Stock_pct = Stock_pct[:-ShapeDiff]
        else:
            Reference_pct = Reference_pct[:-ShapeDiff]
        print("After Adjustment")
        print(Reference_pct.shape)
        print(Stock_pct.shape)

    #find beta
    slope, intercept, r_value, p_value, std_err = linregress(Reference_pct, Stock_pct)
    #print(f"beta = {slope:.3}")
    #print(f"R^2 = {r_value:.3}")
    label = r"$R^{2}$" + f" {r_value:.3}"
    beta = slope

    #plot if requested
    if plot == True:    
        x = np.linspace(Reference_pct.min(),Reference_pct.max())
        y = slope * x + intercept

        fig, axs = plt.subplots()
        axs.plot(Reference_pct, Stock_pct, '.')
        axs.plot(x,y,'k',label = label)
        axs.grid(True)
        axs.set_xlabel('dS/S')
        axs.set_ylabel('dR/R')
        axs.set_title(f"Beta of {StockName[14:-4]} to {ReferenceName[14:-4]}")
        axs.legend()
        plt.show()
    return([beta, r_value]) 

def listStocks(dir = "./correlation", fileName = "data.csv"):
    
    headers = []
       
    RawStockData = pd.read_csv(f"{dir}/{fileName}") 
    for stock in RawStockData.columns:
        if stock.endswith('3'):
            headers.append(stock)
 
    return headers


if __name__ == "__main__":
    
    grabData(1)
    dir = "./correlation"

    StockClose = listStocks()

    for index in StockClose:
      
        beta, r_val = BetaWeightedDelta(dir,index, "XIU.TO.3",plot=False)
        
        print(f"{index[:-5]}     {beta:5.3}  {r_val:5.3}")

    
