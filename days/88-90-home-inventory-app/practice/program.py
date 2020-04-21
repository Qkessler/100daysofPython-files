import app


if __name__ == '__main__':
    app.init_db()
    print('Welcome to Computer Creator!')
    print('----------------------------')
    print()
    menu = app.get_menu()
    menu['1'].function()
    print('Press q to exit.')
    choice = input('Select your choice: ')
    print()
    first = 1
    while choice.lower() != 'q':
        if first != 1:
            print('Press q to exit.')
            choice = input('Select your choice: ')
            print()
        menu[choice].function()
        first = 0
