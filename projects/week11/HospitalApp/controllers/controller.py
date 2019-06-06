import binascii
import sys
sys.path.append('../')
from hashlib import sha256
from utils.database import Database
from models.user_model import User
from models.doctor_model import Doctor
from models.patient_model import Patient

class MainController:
    db = Database()
    curr_user = None
    @classmethod
    def login(cls, username, password):
        password = hash(password)
        if cls.db.check_username_password_match(username, password):
            cls.curr_user = User.login(username, password)
            return 1
        else:
            print('Invalid username or password')
            return -1
        
            
    @classmethod
    def register(cls, **kwargs):
        if cls.db.check_does_user_exist(kwargs['username']):
            print('this user already exists')
        else:
            if kwargs['user_type'] == 'doctor':
                #create doctor
                hashed_password = hash(kwargs['password'])
                cls.curr_user = Doctor.create_doctor(kwargs['uid'], kwargs['username'], hashed_password, kwargs['full_name'], kwargs['specialty'], kwargs['phone_number'])
                
            elif kwargs['user_type'] == 'patient':
                #create patient
                hashed_password = hash(kwargs['password'])
                cls.curr_user = Patient.add_patient(kwargs['uid'], kwargs['username'], hashed_password, kwargs['full_name'], kwargs['age'])
            else:
                print('Invalid user type')



    # @staticmethodfrom hashlib import sha256
    # def hash(inpt):from hashlib import sha256
    #     m = sha256()
    #     m.update(inpt.encode('utf-8'))
    #     return str(m.hexdigest())
    @staticmethod
    def hash(string):
        bina = binascii.unhexlify(string)
        hash = sha256(sha256(bina).digest()).digest()
        raw = str(binascii.hexlify(hash))[2:-1]
        return raw