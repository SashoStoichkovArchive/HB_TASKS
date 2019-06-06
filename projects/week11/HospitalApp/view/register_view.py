from sys import path
from getpass import getpass
path.append('../')
from controllers.controller import MainController
class RegisterView:
    register_type = None

    @classmethod
    def show_register_type(cls):
        print('''
        I am:
        * patient
        * doctor
        ''')
        register_type = input()
        register_type = register_type.lower()
        if register_type == 'patient' or register_type == 'doctor':
            cls.register_type = register_type
        else:
            print('invalid user type')
            cls.show_register()

    @classmethod   
    def show_register_info(cls):
        print('******REGISTER******')
        if cls.register_type == 'patient':
            try:
                username = input('Username: ')
                password = getpass(prompt='Password: ')
                #use national identification number as uid
                nin = int(input('NIN: '))
                full_name = input('Full name: ')
                age = int(input('Age: '))
            except ValueError:
                print('Invalid registration details!')
                cls.show_register_info()
            MainController.register(username=username, password=password, uid=nin, full_name=full_name, age=age, user_type = cls.register_type)
        else:
            try:
                username = input('Username: ')
                password = getpass(prompt='Password: ')
                #use national identification number as uid
                nin = int(input('NIN: '))
                full_name = input('Full name: ')
                specialty = input('Specialty: ')
                phone_number = str(input('Phone number: '))
            except ValueError:
                print('Invalid registration details')
                cls.show_register_info()
            MainController.register(username=username, password=password, uid=nin, full_name = full_name, specialty=specialty, phone_number=phone_number, user_type = cls.register_type)


    @classmethod
    def show_register(cls):
        cls.show_register_type()
        cls.show_register_info()
