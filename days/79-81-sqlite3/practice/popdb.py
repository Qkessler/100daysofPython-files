import sqlite3


def insert_data():
    with sqlite3.connect('addressbook.db') as connection:
        c = connection.cursor()
        name = input('Insert the name: ')
        address = input('Insert the address: ')
        phone = input('Insert the phone number: ')
        info = [name, address, phone]
        c.execute("INSERT INTO DETALLES VALUES(?, ?, ?)", info)


def search(query):
    with sqlite3.connect('addressbook.db') as connection:
        c = connection.cursor()
        [print(row[0]) for row in c.execute(query)]


if __name__ == '__main__':
    search("""SELECT name
    FROM DETALLES
    WHERE address = 'Loquesea';
    """)
