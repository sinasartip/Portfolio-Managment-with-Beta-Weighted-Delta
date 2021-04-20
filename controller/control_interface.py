from model.database import database_interface
from controller.controllers import register_controllers
controller_parms = {
    "database_interface" : None
}


class controller():
    def __init__(self):
        self.controllers = register_controllers()
        self._connect_database()

    def _connect_database(self):
        self.database = database_interface.TSQL()
        self.database.connect()

    def user_control(self):
        user_parms = controller_parms
        user_parms["database_interface"] = self.database
        return self.controllers.connect("USERS", **user_parms)
    
    def portfolio_control(self):
        portfolio_parms = controller_parms
        portfolio_parms["database_interface"] = self.database
        return self.controllers.connect("PORTFOLIO", **portfolio_parms), self.user_control()

    def stock_control(self):
        stock_parms = controller_parms
        stock_parms["database_interface"] = self.database
        return self.controllers.connect("STOCK", **stock_parms)
 