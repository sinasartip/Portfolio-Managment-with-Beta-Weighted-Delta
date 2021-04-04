import unittest
import pyodbc

class Test_DataBase(unittest.TestCase):
    def setUp(self):
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-O5IL6FT\WINDOWS10;DATABASE=portfolio-manager;UID=pythonApp;PWD=J!RRBT&*SyQ!')
        self.cursor = cnxn.cursor()

    def test_select(self):
        self.cursor.execute("select user_id, user_name, total_capital from users")
        row = self.cursor.fetchone()
        if row:
            print(row)

if __name__ == "__main__":
    unittest.main()