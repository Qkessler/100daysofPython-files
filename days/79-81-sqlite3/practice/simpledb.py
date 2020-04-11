import sqlite3


connection = sqlite3.connect('addressbook.db')
c = connection.cursor()
c.execute('''
CREATE TABLE DETALLES(name TEXT, address TEXT, phone_number INT)
''')

connection.close()
