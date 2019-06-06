from sys import path, exit
from getpass import getpass
path.append('../')
from controllers.controller import MainController

class LoginView:
    @classmethod
    def show_login(cls):
        #get user input
        try:
            user_name = input('Enter username: ')
            password = getpass(prompt='Enter password: ')
            remaining_try = 3
            status = MainController.login(user_name, password)
            #if username and password doesn't match
            if status == -1:
                remaining_try-=1
                if remaining_try > 0:
                    cls.show_login()
                else:
                    exit()

        except Exception:
            print('Login unsuccessful')