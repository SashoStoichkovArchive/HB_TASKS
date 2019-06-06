import sys


from controllers.main_controller import MainController
from interface.main_menu import MainMenu


class StartMenu:
    # sing in & sign up
    # redirect to Main menu
    @classmethod
    def run(cls):
        print("Welcome to Hospital Hack Bulgaria!")
        options = """
Do you want to sign in or sign up?
Options:
1 - sign in
2 - sign up
3 - exit
        """
        print(options)
        start_option = input()
        # TODO check if the option number is correct
        username = input('Username:> ')
        password = input('Password:> ')
        if start_option == '1':

            # TODO hide password
            current_user = MainController.sign_in(username, password)
            if current_user:
                MainMenu.show_options(current_user)
            else:
                print("Wrong username or password!")
                sys.exit(1)
        elif start_option == '2':
            # TODO hide password
            second_password = input('Second Password:>')
            try:
                current_user = MainController.sign_up(
                    username, password, second_password)
            except UserAlreadyExistsError:
                print('Sign up failed! User already exists!')
                sys.exit(1)
            except DatabaseConnectionError:
                print('Sign up failed! Server error! Try again')
                sys.exit(1)
            except PasswordsDontMatchError:
                print('Sign up failed! Password don\'t match! Try again')
                sys.exit(1)
            else:
                MainMenu.show_options(current_user)
        else:
            sys.exit(1)