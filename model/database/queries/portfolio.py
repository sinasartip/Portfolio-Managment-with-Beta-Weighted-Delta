
def add_position(portfolio_id, stock_name, position_size):
    command = f'''
        USE portfolio_manager;

        INSERT INTO dbo.portfolio
                ([portfolio_id]
                ,[stock_name]
                ,[position_size])
        VALUES({portfolio_id},'{stock_name}', {position_size});
        '''
    return command

def get_portfolio(portfolio_id):
    print(f"asking for portfolio {portfolio_id}")
    command = f'''
        SELECT *
        FROM portfolio_manager.dbo.portfolio AS portfolio_tb
        WHERE portfolio_tb.[portfolio_id] = {portfolio_id};
        '''
    return command

def remove_position(portfolio_id, stock_name):
    command = f'''
        USE portfolio_manager;

        DELETE FROM dbo.portfolio
        WHERE dbo.portfolio.[portfolio_id] = {portfolio_id}
            AND dbo.portfolio.[stock_name] = {stock_name};
        '''
    return command

def remove_portfolio(portfolio_id):
    command = f'''
        USE portfolio_manager;

        DELETE FROM dbo.portfolio
        WHERE dbo.portfolio.[portfolio_id] = {portfolio_id};
        '''
    return command

def get_corr_matrix():
    pass