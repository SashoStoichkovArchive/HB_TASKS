import sqlite3

def create_user_table():
    connection = sqlite3.connect('course.db')
    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS User
            (id PRIMARY KEY, name Text)
        """
    )

    connection.commit()
    connection.close()

def insert_user(id, name):
    connection = sqlite3.connect('course.db')
    cursor = connection.cursor()
    cursor.execute(
        """
        INSERT INTO User VALUES('{id}', '{name}');
        """.format(id=id, name=name)
    )

    connection.commit()
    connection.close()

def select_user():
    connection = sqlite3.connect('course.db')
    cursor = connection.cursor()

    cursor.execute("SELECT id, name FROM User")
    user = cursor.fetchone()

    connection.commit()
    connection.close()

    return user


def select_users():
    connection = sqlite3.connect('course.db')
    cursor = connection.cursor()

    cursor.execute("SELECT id, name FROM User")
    users = cursor.fetchall()

    connection.commit()
    connection.close()

    return users