import unittest
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from model.CorrelationCoeff import correlationMatrix
from model.Simulator.StockDataGenerator import GBM_PriceGenerator


class TestCorrMatrix(unittest.TestCase):
    def setUp(self):
        self.StockData = self.GenerateStockData()
        self.corrMatrix = correlationMatrix(self.StockData)

    def test_data(self):
        self.plot_data()

    def GenerateStockData(self):
        """Generate equal number of data points for two pretend stocks,
        the two stocks use the same initial state and interest rates, so 
        a high correlation is excpected."""
        self.data_points = 100
        Price_genA = GBM_PriceGenerator(10,20,8)
        Price_genB = GBM_PriceGenerator(10,20,8)
        ABC = np.zeros((self.data_points))
        XYZ = np.zeros((self.data_points))
        for i in range(self.data_points):
            ABC[i] = Price_genA.generate_value()
            XYZ[i] = Price_genB.generate_value()
        return pd.DataFrame(dict(time=np.arange(self.data_points),
                                ABC = ABC, XYZ = XYZ))

    def plot_data(self):
        df = self.StockData
        sns.relplot(x = "time", y="value", hue="variable", kind="line", data=pd.melt(df, ['time']))
        plt.show()

if __name__ == "__main__":
    unittest.main()