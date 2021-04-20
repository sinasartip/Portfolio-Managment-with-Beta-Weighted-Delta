from model.database.queries.stocks import *
from model.database.database_interface import TSQL
from model.GrabStockData import dataGrabber

class StockBuilder():
    def __init__(self):
        self._instance = None
    
    def __call__(self,
                database_interface,
                **_ignored):

        if not self._instance:
            self._instance = Stock(database_interface)
        return self._instance


class Stock():
    def __init__(self, database_interface: TSQL):
        self.database = database_interface

    def get_adjclose(self, portfolio):
        ticker_list = []
        for position in portfolio:
            ticker_list.append(position[1])
        

    def download_prices_todatabase(self, portfolio):
        self.clear_stocks()
        data_grabber = dataGrabber()
        ticker_list = []
        for position in portfolio:
            ticker_list.append(position[1])
        data_grabber.grab_stockData(ticker_list)
        self.database.add_csv_to_table()

    def clear_stocks(self):
        command_string = clear_stocks()
        self.database.execute(command_string)


