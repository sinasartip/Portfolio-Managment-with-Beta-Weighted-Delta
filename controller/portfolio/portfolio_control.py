from model.database.queries.portfolio import *
from model.database.queries import *
from model.database.database_interface import TSQL


class PortfolioBuilder():
    def __init__(self):
        self._instance = None
    
    def __call__(self,
                database_interface,
                **_ignored):

        if not self._instance:
            self._instance = Portfolio(database_interface)
        return self._instance


class Portfolio():
    def __init__(self, database_interface: TSQL):
        self.database = database_interface

    def get_portfolio(self, portfolio_id):
        command_string = get_portfolio(portfolio_id)
        return self.database.execute(command_string, with_return=True)

    def add_position(self, portfolio_id, stock_name, position_size):
        command_string = add_position(portfolio_id, stock_name, position_size)
        self.database.execute(command_string)

    def remove_position(self ,portfolio_id, stock_name):
        command_string = remove_position(portfolio_id, stock_name)
        self.database.execute(command_string)

    def remove_portfolio(self, portfolio_id):
        command_string = remove_position(portfolio_id)
        self.database.execute(command_string)

    def get_corr_matrix(self):
        pass