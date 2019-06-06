import sys
sys.path.append('../')
from models.user_model import User
from utils.database import Database
#in controller validate data and create instance of patient
class Patient(User):
    def __init__(self, uid, username, hashed_password, full_name, age):
        super().__init__(uid, username, hashed_password, 'patient')
        self._age = age
        self._full_name = full_name
    
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

    @property
    def full_name(self):
        return self._full_name

    @full_name.setter
    def full_name(self, value):
        self._full_name = value

    def update_patient(self, **kwargs):
        for kwel, kwval in kwargs.items():
            self.__dict__[kwel] = kwval

    @classmethod
    def add_patient(cls, uid, username, hashed_password, full_name, age):
        super().create_user(uid, username, hashed_password, 'patient')

        #todo: check kwargs
        cls.db.create_new_patient( uid, full_name, age )
        return Patient(uid, username, hashed_password, full_name, age)