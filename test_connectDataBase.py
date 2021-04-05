import unittest
import pyodbc
from model.database.database_interface import TSQL

class Test_DataBase(unittest.TestCase):
    def setUp(self):
        self.database = TSQL()
        self.database.connect()

    def test_select(self):
        self.database.cursor.execute("select user_id, user_name, total_capital from users")
        row = self.database.cursor.fetchone()
        if row:
            print(row)

    def test_add_price(self):
        self.database.csv_to_table()

if __name__ == "__main__":
    unittest.main()