import pandas as pd
import numpy as np
import itertools


class correlationMatrix():
    def __init__(self, ClosingPrice: pd.DataFrame):
        """
        provide a dataframe with the stock tickers and closing prices. 
        The length does not matter but should be equal. If not equal the longer dataset is trimmed down.
        """
        self.stock_price = ClosingPrice
        self.stock_price = self.get_individual_stocks()
        self.corr_frame = self.correlation_coeffitent()

    def get_individual_stocks(self):
        return self.stock_price.iloc[:,1:]    

    def correlation_coeffitent(self):
        return self.stock_price.corr()

    def generate_visualMatrix(self):
        pass