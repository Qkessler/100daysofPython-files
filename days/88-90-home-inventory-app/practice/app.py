from collections import namedtuple
import sqlite3
from contextlib import contextmanager
import os.path

Menu_Element = namedtuple('Menu_Element', 'function name')
db = 'computer_creator.db'
menu = {}


def init_db():
    if os.path.exists('./computer_creator.db'):
        pass
    else:
        with sqlite3.connect(db) as connection:
            cursor = connection.cursor()
            cursor.execute('CREATE TABLE COMPUTER (name TEXT, price INT)')
            connection.commit()


def get_menu():
    menu['1'] = Menu_Element(show_menu, 'Show Menu')
    menu['2'] = Menu_Element(add_part, 'Add Part')
    menu['3'] = Menu_Element(update_part, 'Update Part')
    menu['4'] = Menu_Element(sum_components, 'Total sum')
    return menu


def show_menu():
    print("\n".join([f'{key}: {element.name}'
                     for key, element in menu.items()]))
    print()


def scrub(name):
    return "".join([c for c in name if c.isalnum()])


@contextmanager
def access_db():
    try:
        connection = sqlite3.connect(db)
        cursor = connection.cursor()
        yield cursor
    finally:
        connection.commit()
        connection.close()


def add_part():
    name = input('Which part you are trying to add? ')
    scrub_name = scrub(name)
    price = input('Which was the price you payed for it? ')
    scrub_price = scrub(price)
    with access_db() as c:
        c.execute("INSERT INTO 'COMPUTER' VALUES(?, ?)",
                  [scrub_name, scrub_price])
    print(f'Row added: [name = {scrub_name}, price = {scrub_price}]')
    print()


def update_part():
    pass


def sum_components():
    with access_db() as cursor:
        cursor.execute('SELECT price FROM COMPUTER')
    print(sum(cursor))
    print()
