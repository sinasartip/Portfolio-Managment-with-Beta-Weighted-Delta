import pyodbc


class TSQL():
    """
    TSQL allows you to setup your connection to the database server
        note that you can overide all parameters even using different data
        base engines.
    """
    def __init__(self):
        self.parms = {"driver":'DRIVER={ODBC Driver 17 for SQL Server};',
                    "server":'SERVER=DESKTOP-O5IL6FT\WINDOWS10;',
                    "database":'DATABASE=portfolio-manager;',
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

    def csv_to_table(self):
        """
        Use to change your yfinance csv files to sql tables.
        The table in the database is -> stock_price
        with the following attributes: stock_name, price, date
        """
        
        
