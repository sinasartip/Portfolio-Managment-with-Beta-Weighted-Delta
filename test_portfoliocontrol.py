from controller.portfolio.portfolio_control import Portfolio
import unittest
import random
import itertools
from controller.control_interface import controller
from random_username.generate import generate_username

def add_user():
    user_name = generate_username(1)[0][:-1]
    total_capital = random.randrange(10000,100000)
    return user_name, total_capital


class TestPortfolio(unittest.TestCase):
    def setUp(self):
        self.controller_interface = controller()
        self.portfolio_control, self.user_control = self.controller_interface.portfolio_control()
        self.stock_control = self.controller_interface.stock_control()


    def dtest_aadd_user_position(self):
        print("-----Create positions and delete the new user and portfolio-----")

        self.user_name, self.total_capital = add_user()
        self.user_control.add_user(self.user_name, self.total_capital)
        
        self.users_stocks = {"REI-UN.TO":self.total_capital*0.5, "AAPL":self.total_capital*0.10, 
                            "TJX":self.total_capital*0.15, "DOL.TO":self.total_capital*0.25}

        self.portfolio_id = self.user_control.get_user(self.user_name)[2]
                
        for stock_name, position_size in self.users_stocks.items():
            self.portfolio_control.add_position(self.portfolio_id,stock_name, position_size)

        index = 0       
        keys = list(self.users_stocks.keys())
        positions = self.portfolio_control.get_portfolio(self.portfolio_id) 

        for position in positions:
            self.assertEqual(position[1], keys[index], msg = "stock name not correct")
            self.assertAlmostEqual(position[2], self.users_stocks[keys[index]], places=1, msg="stock price not correct")
            index+=1

    def test_abddportfolio_tostocks(self):
        user = self.user_control.get_user()
        portfolio_id = user[2]
        portfolio = self.portfolio_control.get_portfolio(portfolio_id)
        self.stock_control.download_prices_todatabase(portfolio)

if __name__ == "__main__":
    unittest.main()