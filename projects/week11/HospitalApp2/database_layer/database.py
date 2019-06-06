from utils.constants import DataBaseConstants

DATABASE_ENGINE = DataBaseConstants.ENGINE
DATABASE_NAME = DataBaseConstants.NAME

# @atomic_transaction
class Database:
    
    def __init__(self):
        self.connection = DATABASE_ENGINE.connect(DATABASE_NAME)
        self.cursor = self.connection.cursor
        self.cursor.row_factory = DATABASE_ENGINE.Row

    def create(self, model_name, **kwargs):
        pass

    def find(self):
        pass