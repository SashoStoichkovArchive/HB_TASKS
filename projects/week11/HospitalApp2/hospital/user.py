class User:

    def __init__(self, username, password, status=None, email=None):
        self.username = username
        self.password = password
        self._status = status
        self._email = email

    @property
    def status(self):
        return self._status

    @property
    def email(self):
        return self._email