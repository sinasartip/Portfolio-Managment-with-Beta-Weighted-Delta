from controller.control_interface import controller, controller_parms

class flags():
    def __init__(self):
        pass
    def set_flags(self):
        self.exit = False

if __name__ == "__main__":
    flags = flags()
    flags.set_flags()
    controller = controller()

    #ask what you want to do
    #new user
    #enter user info:
    #username : sina_sartip
    #total_capital : $10,000

    #call controller user 
    user = controller.user_control()
    user.