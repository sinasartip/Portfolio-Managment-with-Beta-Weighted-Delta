import unittest
import random
import itertools
from controller.control_interface import controller
from random_username.generate import generate_username


class TestUser(unittest.TestCase):
    def setUp(self):
        self.controller_interface = controller()
        self.user_control = self.controller_interface.user_control()

    def test_adduser(self):
        print("-----This test will add a new user with random username-----")

        user_name = generate_username(1)[0][:-1]
        total_capital = random.randrange(10000,100000)

        self.user_control.add_user(user_name, total_capital)

        query_result = self.user_control.get_user(user_name)

        print("checking user name...")
        self.assertEqual(query_result[0][1], user_name, msg="the user name was not seen in database")
        print("checking total capital...")
        self.assertEqual(query_result[0][3], total_capital, msg="the total capital was not added correctly in database")

        print("user name  and captial correct!")

    def test_get_all_users(self):
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

    def test_delete_user(self):
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