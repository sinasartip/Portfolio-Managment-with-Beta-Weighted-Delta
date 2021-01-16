import unittest
from model.GrabStockData import dataGrabber

class Test_GrabStockData(unittest.TestCase):
    def test_grabStockData(self):
        self.stocks = dataGrabber("stocks")
        
        self.stocks.read_stockFile()
        print(self.stocks.tickerList)
        
        self.stocks.grab_stockData()
        print(self.stocks.StockData.head)


    def test_saveStockData(self):
        self.stocks = dataGrabber("stocks")
        
        self.stocks.read_stockFile()
        print(self.stocks.tickerList)
        
        self.stocks.grab_stockData()
        print(self.stocks.StockData.head)

        self.stocks.save_stockData()
        
    def load_stockData(self):
        pass

if __name__ == "__main__":
    unittest.main()