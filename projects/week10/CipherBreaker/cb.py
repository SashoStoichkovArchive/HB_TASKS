import sqlite3
from itertools import product as p
from string import digits as d
from string import ascii_letters as l
from secret_keeper import make_it_secret as ms

import time

def generate_strings(length):
    chars = l + d

    for s in p(chars, repeat=length):
        yield ''.join(s)

def generate_message_from_file():
    message = []

    with open('message.txt', 'r') as f:
        for line in f:
            for word in line.split():
                message.append(word)

    return message

def create_table():
    connection = sqlite3.connect('CipherBreaker.db')
    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS CipherBreaker
            (id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, message TEXT, encrypted_message TEXT, index_in_message INTEGER UINQUE);
        """
    )

    connection.commit()
    connection.close()

def add_words():
    connection = sqlite3.connect('CipherBreaker.db')
    cursor = connection.cursor()

    message = generate_message_from_file()
    l = 0

    for i in range(6):
        word_gen = generate_strings(i)

        for word in word_gen:
            if ms(word) in message:
                l += 1

                cursor.execute(
                    """
                    INSERT INTO CipherBreaker (message, encrypted_message, index_in_message) VALUES(?, ?, ?);
                    """, (word, ms(word), message.index(ms(word)))
                )

                connection.commit()

            if l == len(message):
                break

        if l == len(message):
            break

    connection.close()

def message():
    connection = sqlite3.connect('CipherBreaker.db')
    cursor = connection.cursor()

    result = []

    m = cursor.execute(
        """
            SELECT message FROM CipherBreaker ORDER BY index_in_message;
        """
    )

    for word in m:
        result.append(word[0])

    connection.commit()
    connection.close()

    return result


if __name__ == "__main__":
    s = time.time()

    create_table()
    add_words()

    result = message()

    e = time.time()

    print(result[:3])
    print(result[3:7])
    print(result[7:15])
    print(result[15:18])
    print(result[18:20])
    print(result[20:25])

    print('Execution time ', (e-s))