import unittest
import numpy as np
from model.CorrelationCoeff import correlationMatrix


class TestCorrMatrix(unittest.TestCase):
    def setUp(self):
        self.StockData = self.GenerateStockData()
        self.corrMatrix = correlationMatrix(self.StockData)

    def GenerateStockData(self):
        return 1 

if __name__ == "__main__":
    unittest.main()