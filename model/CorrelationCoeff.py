import pandas as pd

class correlationMatrix():
    def __init__(self, ClosingPrice: pd.DataFrame):
        """
        provide a dataframe with the stock tickers and closing prices. 
        The length does not matter but should be equal. If not equal the longer dataset is trimmed down.
        """
        print(ClosingPrice.head)

    def get_closing_price(self):
        pass

    def correlation_coeffitent(self):
        pass

    def generate_matrix(self):
        pass