class UserAlreadyExistsError(Exception):
    
    def __init__(self, message):

        # Call the base class constructor with the parameters it needs
        super().__init__(message)

class DatabaseConnectionError(Exception):

    def __init__(self, message):

        # Call the base class constructor with the parameters it needs
        super().__init__(message)

class PasswordsDontMatchError(Exception):
    
    def __init__(self, message):

        # Call the base class constructor with the parameters it needs
        super().__init__(message)

class InvalidPasswordError(Exception):
    
    def __init__(self, message):

        # Call the base class constructor with the parameters it needs
        super().__init__(message)