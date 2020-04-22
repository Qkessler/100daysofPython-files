from collections import namedtuple
import sqlite3
from contextlib import contextmanager
import os.path
import re
import sys

Menu_Element = namedtuple('Menu_Element', 'function name')
db = 'computer_creator.db'
menu = {}
pat_price = re.compile(r'\d+')


def init_db():
    if os.path.exists('./computer_creator.db'):
        pass
    else:
        with sqlite3.connect(db) as connection:
            cursor = connection.cursor()
            cursor.execute('CREATE TABLE COMPUTER (name TEXT, price INT)')
            connection.commit()


@contextmanager
def access_db():
    try:
        connection = sqlite3.connect(db)
        cursor = connection.cursor()
        yield cursor
    finally:
        connection.commit()
        connection.close()


def get_menu():
    menu['1'] = Menu_Element(show_menu, 'Show Menu')
    menu['2'] = Menu_Element(add_part, 'Add Part')
    menu['3'] = Menu_Element(list_parts, 'List Parts')
    menu['4'] = Menu_Element(update_part, 'Update Part')
    menu['5'] = Menu_Element(sum_components, 'Total sum')
    menu['q'] = Menu_Element(sys.exit, 'Exit')
    return menu


def list_parts():
    with access_db() as cursor:
        cursor.execute('SELECT name, price FROM COMPUTER')
        print("\n".join([f'- {name}: ${price}' for name, price in cursor]))
    print()


def show_menu():
    print("\n".join([f'{key}: {element.name}'
                     for key, element in menu.items()]))
    print()


def scrub(name):
    return "".join([c for c in name if c.isalnum()])


# Input checker implemented.
def add_part():
    name = input('Which part are you trying to add? ')
    scrub_name = scrub(name)
    while not scrub_name:
        name = input('Please input a correct name: ')
        scrub_name = scrub(name)
    price = input('Which was the price you payed for it? ')
    scrub_price = scrub(price)
    while not pat_price.match(scrub_price):
        price = input('Please input a correct price: <number>\n')
        scrub_price = scrub(price)
    with access_db() as c:
        c.execute("INSERT INTO 'COMPUTER' VALUES(?, ?)",
                  [scrub_name, scrub_price])
    print(f'Row added: [name = {scrub_name}, price = {scrub_price}]')
    print()


def update_part():
    list_parts()
    options = ['name', 'price']
    dict_options = {'name': re.compile('.+'), 'price': pat_price}
    att = input('Which column do you want to update? Options: %s\n' % options)
    while att not in options:
        att = input('Options: %s\n' % options)
    row_content = input('Which row do you want to change? ')
    value = input('What is the correct value? ')
    comprob = dict_options.get(att)
    while not comprob.match(value):
        value = input('Please input a correct value: ')
    print(f'att = {att}, value = {value}, row_content = {row_content}')
    query = "UPDATE COMPUTER SET " + att + " = "+value+" WHERE " + att + " = " + row_content
    print(query)
    with access_db() as c:
        c.execute(query)
    list_parts()


def sum_components():
    with access_db() as cursor:
        cursor.execute('SELECT price FROM COMPUTER')
    sum_rows = 0
    for row in cursor:
        sum_rows += row
    print(sum_rows)
    print()
