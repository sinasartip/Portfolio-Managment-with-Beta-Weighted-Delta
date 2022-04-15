from warnings import resetwarnings
import pyodbc
import pandas as pd


class TSQL():
    """
    TSQL allows you to setup your connection to the database server
        note that you can overide all parameters even using different data
        base engines.
    """
    def __init__(self):
        self.parms = {"driver":'DRIVER={ODBC Driver 17 for SQL Server};',
                    "server":'SERVER=DESKTOP-O5IL6FT\WINDOWS10;',
                    "database":'DATABASE=portfolio_manager;',
                    "uid":'UID=pythonApp;',
                    "pwd":'PWD=J!RRBT&*SyQ!'}

    def connect(self):
        """
        By connecting you will only know that the connection was successful. 
        No information in known of the actual data inside the database. 
        """
        setup = f"{self.parms['driver']}{self.parms['server']}{self.parms['database']}{self.parms['uid']}{self.parms['pwd']}"
        self.cnxn = pyodbc.connect(setup)
        self.cursor = self.cnxn.cursor()

    def add_csv_to_table(self):
        """
        Use to change your yfinance csv files to sql tables.
        The table in the database is -> stock_price
        with the following attributes: stock_name, price, date
        """
        #TODO: check if connection has already been made and csv file exists
        #TODO: parse database name
        #TODO: fix row[3]

        self.SQL_ready_df = pd.read_csv('./model/csv_data/SQLReady_Stock_Data.csv')
        
        self.cursor.execute('''DELETE FROM portfolio_manager.dbo.stock_price;''')
        
        for row in self.SQL_ready_df.itertuples():
            self.cursor.execute('''
                INSERT INTO portfolio_manager.dbo.stock_price (
                [date],
                [ticker],
                [adj_close],
                [perd_close],
                [high],
                [low],
                [perd_open],
                [volume])
                VALUES (?,?,?,?,?,?,?,?)
                ''',
                row.Date,row.Ticker,row[3],row.Close,row.High,row.Low,row.Open,row.Volume)
            self.cnxn.commit()

    def execute(self, command, with_return = False, num_of_rows = None):
        """
        will execute your query and return a pandas dataframe containing the table is a select is done.
        """
        if not with_return:
            self.cursor.execute(command)
            self.cursor.commit()
        else:
            if num_of_rows:
                self.cursor.execute(command)
                return self.cursor.fetchmany(num_of_rows)
            else:
                self.cursor.execute(command)
                return self.cursor.fetchall() 
        
