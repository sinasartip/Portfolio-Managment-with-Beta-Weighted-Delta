from helper_functions import object_factory
from controller.user.user_control  import UserBuilder
from controller.portfolio.portfolio_control import PortfolioBuilder
from controller.stock.stock_control import Stock, StockBuilder

# Omitting other implementation classes shown above
class Controller(object_factory.ObjectFactory):
    def connect(self, ID, **kwargs):
        return self.create(ID, **kwargs)

def register_controllers():
    controllers = Controller()
    controllers.register_builder('USERS', UserBuilder())
    controllers.register_builder('PORTFOLIO', PortfolioBuilder())
    controllers.register_builder('STOCK', StockBuilder())
    # controllers.register_builder('PTT_STREAM', create_local_music_service)
    return controllers