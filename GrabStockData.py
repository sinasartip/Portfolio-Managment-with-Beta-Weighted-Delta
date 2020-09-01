import yfinance as yf
import os 
import shutil
import numpy as np

def grabData(TickerList, linesToSkip):
    """grab data from yahoo finance (not official yahoo finance api)
      
    """
    if os.path.exists("./correlation"):
        shutil.rmtree("correlation",ignore_errors=True)
        os.mkdir("correlation")
        os.chdir("./correlation")
    else: 
        os.mkdir("correlation")
        os.chdir("./correlation")
    
    print(os.getcwd())
    for _ in range(linesToSkip):
        next(TickerList)

    TickerList = TickerList.readlines()
    symbols = []
    for ticker in TickerList:         
        symbols.append(f"{ticker.rstrip()}.TO")

    data = yf.download(symbols,period='3mo',interval='1d',group_by='ticker',threads=True)
   
    print(data)
    data.to_csv('data.csv')
    




if __name__ == "__main__":

    #grab list of stocks to check 
    TickerList = open("stocks.txt", "r")
    grabData(TickerList, 1)
    