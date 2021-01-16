from math import sqrt, exp
from random import gauss, seed


class GBM_PriceGenerator():
    def __init__(self, initial_price, annual_interest, volatility):
        self.initial_price = initial_price
        self.interest_rate = annual_interest
        self.volatility = volatility

    def generate_value(self):
        current_price = self.initial_price
        mu = self.interest_rate
        sigma = self.volatility

        current_price *= exp((mu - 0.5 * sigma**2) * (1.0/365.0) * gauss(mu = 0, sigma = 1))
        return current_price
