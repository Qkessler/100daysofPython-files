from collections import namedtuple
import sqlite3
from contextlib import contextmanager

Menu_Element = namedtuple('Menu_Element', 'function name')
db = 'computer_creator.db'


def init_db():
    with sqlite3.connect(db) as connection:
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE COMPUTER ()')

def get_menu():
    menu = {}
    menu['1'] = Menu_Element(add_part(), 'Add Part')
    menu['2'] = Menu_Element(update_part(), 'Update Part')
    menu['3'] = Menu_Element(sum_components(), 'Total sum')


def scrub(name):
    return "".join([c for c in name if c.isalnum()])


@contextmanager
def access_db():
    try:
        connection = sqlite3.connect(db)
        cursor = connection.cursor()
        yield cursor
    finally:
        cursor.commit()
        connection.close()


# modify
def add_part():
    name = input('Which part you are trying to add? ')
    scrub_name = scrub(name)
    with access_db() as c:
        c.execute("CREATE TABLE '" + scrub_name + "' ()")


def update_part():
    
