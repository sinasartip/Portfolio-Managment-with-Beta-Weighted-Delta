

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
    command = f'''
    SELECT *
    FROM portfolio_manager.dbo.users
    WHERE users.user_name = '{user_name}';
    '''
    return command

def add_user(user_name, capital):
    command = f'''
        USE portfolio_manager;

        INSERT INTO dbo.users
                ([user_name]
                ,[total_capital])
        VALUES('{user_name}',{capital});
        '''
    return command

def delete_user(user_name = None, last_user = False):
    if last_user or not user_name:
        command = f'''
        USE portfolio_manager;

        DELETE FROM dbo.users
        WHERE users.user_id = (SELECT MAX([user_id]) AS max_id
                      FROM [portfolio_manager].[dbo].[users]);
        '''
    else:
        command = f'''
        USE portfolio_manager;

        DELETE FROM portfolio_manager.dbo.users
        WHERE users.user_name = '{user_name}';
        '''

    return command