from sqlalchemy import create_engine

engine = create_engine('sqlite:///my_users', echo=True)