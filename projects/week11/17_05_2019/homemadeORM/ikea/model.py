class BaseModelMetaClass(type):
    pass

class Column:
    constraints = ()

    def __init__(self, unique=False):
        self.unique = unique

    def get_constraints(self):
        return ''.join(self.constraints)

    def as_sql(self, name):
        constraints_str = self.get_constraints()
        unique_str = self.unique and 'UNIQUE' or ''
        return f'{name} {self.column_type} {constraints_str} {unique_str}'

class PKColumn(Column):
    column_type = 'INTEGER'

    constraints = (
        'PRIMARY KEY',
        'AUTOINCREMENT'
    )

class TextColumn(Column):
    column_type = 'TEXT'

class BaseModel(metaclass=BaseModelMetaClass):
    id = PKColumn()

    def __init__(self):
        self.columns = {}

        for key, value in self.__class__.__dict__.items():
            if isinstance(value, Column):
                self.columns[key] = value

    # def create_table(self):
    #     return f'''
    #     CREATE TABLE {self.__tablename__}(

    #     )
    #     '''


class User(BaseModel):

    __tablename__ = 'users'

    full_name = TextColumn()