from collections import namedtuple
import sqlite3

Menu_Element = namedtuple('Menu_Element', 'function name')
db = 'computer_creator.db'


def get_menu():
    menu = {}
    menu['1'] = Menu_Element()
    menu['2']


def scrub(name):
    return "".join([c for c in name if c.isalnum()])


def access_db():
    try:
        connection = sqlite3.connect(db)
        cursor = connection.cursor()
        yield cursor
    finally:
        cursor.commit()
        connection.close()


def add_part():
    name = input('Which part you are trying to add? ')
    scrub_name = scrub(name)
    with access_db() as c:
        c.execute("CREATE TABLE '" + scrub_name + "' ()")
