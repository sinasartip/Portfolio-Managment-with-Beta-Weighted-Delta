import pandas as pd
import numpy as np


class correlationMatrix():
    def __init__(self, ClosingPrice: pd.DataFrame):
        """
        provide a dataframe with the stock tickers and closing prices. 
        The length does not matter but should be equal. If not equal the longer dataset is trimmed down.
        """
        self.stock_price = ClosingPrice
        print(self.stock_price.head)
        self.stock_nparray = self.get_individual_stocks()
        self.correlation_coeffitent()

    def get_individual_stocks(self):
        num_of_tickers = np.shape(self.stock_price)[1]
        num_of_datapoints = np.shape(self.stock_price)[0]
        stocks = np.zeros((num_of_datapoints, num_of_tickers-1))

        index = 1
        for _ in self.stock_price.iloc[0,1:]:
            stocks[:,index-1] = self.stock_price.iloc[:,index]
            index+=1
        self.num_of_tickers = num_of_tickers-1
        return stocks

    def correlation_coeffitent(self):
        #add a combinations function to let you add more stocks.
        corr_mat = np.corrcoef(self.stock_nparray[:,0],self.stock_nparray[:,1])
        print(corr_mat)

    def generate_matrix(self):
        pass