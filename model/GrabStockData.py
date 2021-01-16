import yfinance as yf
import os 
import shutil
import numpy as np


class dataGrabber():
    def __init__(self, stockList_fileName):
        self.set_defaultFlags()
        self.stock_file = stockList_fileName
        self.stockFile_address = f"./model/{self.stock_file}.txt"
        self.check_file_exists()
            
    def set_defaultFlags(self):
        self.stockList_exists = False
        self.fileNotAccessible = False

    def check_file_exists(self):
        self.stockList_exists = os.path.exists(self.stockFile_address)

    def read_stockFile(self):
        self.tickerList = []
        try:
            with open(self.stockFile_address) as stockFile:
                stockList = stockFile.readlines()
                
                for ticker in stockList[1:]:         
                    #last item on the ticket list may be a new line character
                    if ticker == '\n':
                        pass
                    else:
                        self.tickerList.append(f"{ticker.rstrip()}")

        except IOError:
            print("File not accessible")
            self.fileNotAccessible = True

    def grab_stockData(self):
        self.StockData = yf.download(self.tickerList,period='1mo',interval='1d',group_by='ticker',threads=True)

    def load_stockData(self):
        pass

    def save_stockData(self):
        self.StockData.to_csv('Stock_Data.csv')
    


