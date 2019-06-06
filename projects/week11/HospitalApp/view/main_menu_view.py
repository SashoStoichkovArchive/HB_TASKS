import traceback
from login_view import LoginView
from register_view import RegisterView
class MainMenuView:
    @staticmethod
    def show_options():
        MAIN_MENU={
        1: LoginView.show_login,
        2: RegisterView.show_register
        }
        #print menu
        print("""
        1 - Login
        2 - Register
        """)

        #get user input
        try:
            selected = int(input('Select option: '))
            if selected < 1 or selected > 2:
                raise ValueError
            action = MAIN_MENU.get(selected, lambda: "Invalid option")
            action()
        except ValueError as e:
            tb = traceback.format_exc()
            print('Invalid option!')
            print(e, tb)
        

if __name__ == '__main__':
    MainMenuView.show_options()