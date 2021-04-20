import yfinance as yf
import os 
import shutil
import numpy as np
import pandas as pd


class dataGrabber():
    def grab_stockData(self, ticker_list):
        ticker_string = ""
        for ticker in ticker_list:
            ticker_string += ticker
            ticker_string += " "
        self.StockData = yf.download(ticker_string, period='1mo', interval='1d', group_by='ticker', threads=True)
        self.save_stockDataTSQL()

    def load_stockData(self,SQL=True):
        #TODO try block for no csv file
        if SQL:
            self.SQL_ready_df = pd.read_csv('./model/csv_data/SQLReady_Stock_Data.csv')
        else:
            self.StockData = pd.read_csv('./model/csv_data/Stock_Data.csv')    

    def save_stockDataRAW(self):
        self.StockData.to_csv('./model/csv_data/Stock_Data.csv')
    
    def save_stockDataTSQL(self):
        self.SQL_ready_df = self.StockData.stack(level=0).rename_axis(['Date', 'Ticker']).reset_index(level=1) #fix for multilevel column issue of yfinance
        self.SQL_ready_df = self.SQL_ready_df.round({"Adj Close":4, "Close":4, "High":4, "Low":4, "Open":4})
        self.SQL_ready_df.to_csv('./model/csv_data/SQLReady_Stock_Data.csv')       

