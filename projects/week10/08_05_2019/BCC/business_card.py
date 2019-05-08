import sqlite3, sys, os, pprint

def print_menu():
    c = str(input(">>> Enter command: "))

    if c == 'help':
        print(
"""
#############
###Options###
#############

1. `add` - insert new business card
2. `list` - list all business cards
3. `get` - display full information for a certain business card (`ID` is required)
4. `delete` - delete a certain business card (`ID` is required)
5. `help` - list all available options
6. `exit` - exit the program
"""
        )

    elif c == 'add':
        os.system('cls' if os.name == 'nt' else 'clear')
        add_business_card()

    elif c == 'list':
        os.system('cls' if os.name == 'nt' else 'clear')
        list_business_cards()

    elif c == 'get':
        os.system('cls' if os.name == 'nt' else 'clear')
        id = int(input("Enter id: "))        
        get_business_card(id)

    elif c == 'delete':
        os.system('cls' if os.name == 'nt' else 'clear')
        id = int(input("Enter id: "))
        delete_business_card(id)

    elif c == 'exit':
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Goodbye!")
        sys.exit(0)        

def create_user_table():
    connection = sqlite3.connect('bcc.db')
    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS User
            (id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, name TEXT, email TEXT, age INTEGER, phone TEXT, add_info TEXT);
        """
    )

    connection.commit()
    connection.close()

def add_business_card():
    connection = sqlite3.connect('bcc.db')
    cursor = connection.cursor()

    name = str(input("Enter full name: "))
    email = str(input("Enter email: "))
    age = int(input("Enter age: "))
    phone = str(input("Enter phone: "))
    add_info = str(input("Enter additional info (optional): "))

    cursor.execute(
        """
        INSERT INTO User (name, email, age, phone, add_info) VALUES(?, ?, ?, ?, ?);
        """, (name, email, age, phone, add_info)
    )

    connection.commit()
    connection.close()

def list_business_cards():
    connection = sqlite3.connect('bcc.db')
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT * FROM User;
        """
    )
    pprint.pprint(cursor.fetchall())

    connection.commit()
    connection.close()

def get_business_card(id):
    connection = sqlite3.connect('bcc.db')
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT * FROM User WHERE id=?;
        """, (id,)
    )
    id, name, email, age, phone, add_info = cursor.fetchone()

    print(
"""
Contact Info:

###############
Id: {id},
Full name: {name}
Email: {email}
Age: {age}
Phone: {phone}
Additional info: {add_info}
##############
""".format(id=id, name=name, email=email, age=age, phone=phone, add_info=add_info)
    )

    connection.commit()
    connection.close()

def delete_business_card(id):
    connection = sqlite3.connect('bcc.db')
    cursor = connection.cursor()

    print("Following contact is deleted successfully")
    get_business_card(id)

    cursor.execute(
        """
        DELETE FROM User WHERE id=?;
        """, (id,)
    )

    connection.commit()
    connection.close()

if __name__ == "__main__":
    print("Hello! This is your business card catalog. What would you like? (enter 'help' to list all available options)")
    while True:
        create_user_table()
        print_menu()
