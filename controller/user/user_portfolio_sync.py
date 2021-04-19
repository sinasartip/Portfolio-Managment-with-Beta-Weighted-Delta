
def check_last_portfolio_id(user_obj):
    try:
        last_user = user_obj.get_all_users()[-1]
    except IndexError:
        print("check_last_portfolio_id -> no users in database returning id 1000")
        return 1000
    else:      
        return last_user[2]+1