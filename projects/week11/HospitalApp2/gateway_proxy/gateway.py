from utils.logger import Logger
from database_layer.database import Database

class Gateway:

    log = Logger()
    db = Database()

    def __call__(self):
        pass