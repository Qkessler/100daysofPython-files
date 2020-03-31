import pyperclip
from time import strftime
# The script for day 2 will be a persistent clipboard app.
# I guess the steps to go through are the following:
# DONE : 1. Get the string copied by the user.
# DONE : 2. Store it in a database(in my case I will be using a file).
# TODO : 3. Get the script to be running everytime.


def get_last():
    with open('clipboard.log', 'r') as f:
        lines = f.readlines()
        if len(lines) == 0:
            return None
        return lines[-1].strip().split(':')[-1]


def persistent_clipboard():
    copied = pyperclip.paste()
    time = strftime('%d/%m/%y %T')
    if get_last().strip() != copied:
        with open('clipboard.log', 'a+') as f:
            to_write = f'{time}: {copied}\n'
            f.write(to_write)


if __name__ == '__main__':
    persistent_clipboard()
