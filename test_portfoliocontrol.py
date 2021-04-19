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


    def test_add_user_position(self):
        print("-----Create positions and delete the new user and portfolio-----")
        try:
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
                self.assertEqual(position[1].split(' ')[0], keys[index], msg = "stock name not correct")
                self.assertAlmostEqual(float(position[2]), self.users_stocks[keys[index]], places=1, msg="stock price not correct")
                index+=1
        finally:
            self.user_control.delete_user()

    def dtest_remove_user(self):
        print("-----This test will try 0, rows_available number of rows of all users----")

        num_users = self.user_control.get_numof_users()

        rows_1 = self.user_control.get_all_users(num_users)
        rows_2 = self.user_control.get_all_users(0)
        
        print("checking get all user behaves correctly with 0 and num of user")
        self.assertEqual(rows_1, rows_2, msg="The API no longer has the excpected behaviour")

        print("making sure there was data in the  table...")
        self.assertGreater(len(rows_1), 0, msg="No data came back from the query")
        self.assertEqual(len(rows_2), num_users, msg="the returned was not all available rows")

        print("all users seen as excpected!")

    def dtest_adjust_positions(self):
        print("-----This test will check if intended rows are deleted-----")
        rows = self.user_control.get_all_users()
        self.user_control.delete_user()
        rows_postdel = self.user_control.get_all_users()
        self.assertNotEqual(rows[-1][1], rows_postdel[-1][1], msg="the username was not deleted")

        second_user = self.user_control.get_all_users()[1]
        self.user_control.delete_user(second_user[1])
        rows_postdel = self.user_control.get_all_users()
        before = []
        after = []
        for rowb, rowa in zip(rows, rows_postdel):
            before.append(rowb[1])
            after.append(rowa[1])

        self.assertNotEqual(before, after, msg="the username was not deleted.")


if __name__ == "__main__":
    unittest.main()