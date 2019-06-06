import sys
sys.path.append('../')
from models.user_model import User
from utils.database import Database

class Doctor(User):
    db = Database()
    def __init__(self, uid, username, hashed_password, full_name, specialty, phone_number):
        super().__init__(uid, username, hashed_password, 'doctor')
        self._full_name = full_name
        self._specialty = specialty
        self._phone_number = phone_number
        
    @property
    def specialty(self):
        return self._specialty

    @specialty.setter
    def specialty(self, value):
        self._specialty = value

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        self._phone_number = value

    @classmethod
    def show_patients(cls, uid):
        pass
        #if this uid represents doctor then
        # result = cls.db.show_all_patients(uid)
        #eventualy do smth with result
        # return result

    @classmethod
    def login(cls, username, hashed_password):
        # result = cls.db.
        pass

    def show_examinations_for_day(self):
        pass  

    def show_available_slots(self, date):
        pass

    def search_user_by_id(self, uid):
        pass



    @classmethod
    def create_doctor(cls, uid, username, hashed_password, full_name, specialty, phone_number):
        super().create_user(uid, username, hashed_password, 'doctor')

        #todo: check kwargs
        cls.db.create_new_doctor( uid, full_name, specialty, phone_number )
        return Doctor(uid, username, hashed_password, full_name, specialty, phone_number)