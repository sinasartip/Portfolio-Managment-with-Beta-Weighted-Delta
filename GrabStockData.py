import yfinance as yf
import os 
import shutil
import numpy as np

def grabData(linesToSkip = 1):
    """grab data from yahoo finance (not official yahoo finance api)
      
    """
    TickerList = open("stocks.txt", "r")

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
        #last item on the ticket list may be a new line character
        if ticker == '\n':
            pass
        else:
            symbols.append(f"{ticker.rstrip()}")
            
    
    data = yf.download(symbols,period='1mo',interval='1d',group_by='ticker',threads=True)
   
    
    data.to_csv('data.csv')
   
    os.chdir("../")
    




if __name__ == "__main__":

    #grab list of stocks to check 
    TickerList = open("stocks.txt", "r")
    grabData(TickerList, 1)
    