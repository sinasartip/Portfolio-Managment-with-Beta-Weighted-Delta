

from model.database.queries.portfolio import get_portfolio


def get_all_users(num_of_rows = None):
    if not num_of_rows:
        command = f'''
        SELECT * 
        FROM portfolio_manager.dbo.users;
        '''
    else:
        command = f'''
        SELECT TOP ({num_of_rows}) * 
        FROM portfolio_manager.dbo.users;
        '''
    return command

def get_numof_users():
    
    command = f'''
    SELECT COUNT(user_name) AS num_of_users
    FROM portfolio_manager.dbo.users;
    '''
    return command

def get_user(user_name = None):
    if not user_name:
        command = f'''
        WITH last_userid (max_id) AS
        (
            SELECT MAX([user_id]) AS max_id
            FROM [portfolio_manager].[dbo].[users]
        )
                
        SELECT*
        FROM portfolio_manager.dbo.users
        WHERE users.user_id = (SELECT max_id FROM last_userid);
        '''
    else:
        command = f'''
        SELECT *
        FROM portfolio_manager.dbo.users
        WHERE users.user_name = '{user_name}';
        '''
    return command

def add_user(user_name, capital, portfolio_id):
    command = f'''
        USE portfolio_manager;

        INSERT INTO dbo.users
                ([user_name]
                ,[total_capital]
                ,[portfolio_id])
        VALUES('{user_name}',{capital}, {portfolio_id});
        '''
    return command

def delete_user(user_name = None, last_user = False):
    if last_user or not user_name:
        command = f'''
            WITH last_userid (max_id) AS
            (
                SELECT MAX([user_id]) AS max_id
                FROM [portfolio_manager].[dbo].[users]
            ),
            lastuser_pid (user_id, portfolio_id) AS
            (
                SELECT user_name, portfolio_id
                FROM users
                INNER JOIN last_userid
                    ON last_userid.max_id = users.user_id
            )

            DELETE p
            FROM portfolio AS p
            INNER JOIN lastuser_pid
                ON p.portfolio_id = lastuser_pid.portfolio_id;

            WITH last_userid (max_id) AS
            (
                SELECT MAX([user_id]) AS max_id
                FROM [portfolio_manager].[dbo].[users]
            )
                    
            DELETE FROM portfolio_manager.dbo.users
                WHERE users.user_id = (SELECT max_id FROM last_userid);
        '''
    else:
        command = f'''
            USE portfolio_manager;

            WITH users_portfolio (portfolio_id, user_name)
            AS
            (
                SELECT portfolio_id, user_name
                FROM users
                WHERE user_name = '{user_name}' --place user_name variable
            )

            DELETE p
            FROM portfolio AS p
            INNER JOIN users_portfolio
                ON p.portfolio_id = users_portfolio.portfolio_id;

            DELETE
            FROM users
            WHERE user_name = '{user_name}';
            '''
    return command