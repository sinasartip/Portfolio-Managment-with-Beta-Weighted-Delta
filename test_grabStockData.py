import unittest
from model.GrabStockData import dataGrabber

class Test_GrabStockData(unittest.TestCase):
    def setUp(self):
        self.stocks = dataGrabber("stocks")
        
        self.stocks.read_stockFile()        
        self.stocks.grab_stockData()

    def donttest_grabStockData(self):
        print(self.stocks.StockData.head)


    def test_saveStockData(self):
        print(self.stocks.StockData.head)

        self.stocks.save_stockDataRAW()

    def test_print(self):
        self.stocks.save_stockDataTSQL()    

    def load_stockData(self):
        pass

if __name__ == "__main__":
    unittest.main()