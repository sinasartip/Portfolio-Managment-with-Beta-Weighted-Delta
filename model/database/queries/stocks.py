
def clear_stocks():
    command = f'''
        USE portfolio_manager;

        DELETE FROM dbo.stock_price;
        '''
    return command

def get_adjclose(ticker_list):
    pass