import random
import csv


class Roll():
    def __init__(self, name):
        self.name = name

    def defeat(self, defensor):
        with open('battle-table.csv') as fin:
            reader = csv.DictReader(fin)
            for row in reader:
                if row['Attacker'] == self.name:
                    for key in row['Attacker'].keys():
                        print(key)
                    if row.keys() == 'tie':
                        return 'TIE'
                    elif row.keys()[str(defensor)].strip().lower() == 'win':
                        return 'WIN'
                    else:
                        return 'LOSE'

    def __str__(self):
        return self.name


class Player():
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Player_' + self.name


class Game():
    def __init__(self):
        self.lives = 3

    def main(self):
        self.setup()
        self.game_loop()

    def setup(self):
        print('--------------------------')
        print('Rock, paper, Scissors Game')
        print('--------------------------')
        print()

    def game_on(self):
        return self.lives > 0

    def decrement_lives(self):
        self.lives -= 1

    def game_loop(self):
        choices = []
        names = []
        with open('battle-table.csv', 'rU') as fin:
            reader = csv.DictReader(fin)
            for row in reader:
                choices.append(Roll(row["Attacker"]))
                names.append(row["Attacker"])

        with open('battle-table.csv') as fin:
            reader = csv.DictReader(fin)
            for row in reader:
                if row["Attacker"] == "Air":
                    for key in row.keys():
                        print(row[key])
        # print('Welcome to the game of RPS!')
        # print('What is your name?')
        # name = input("- ")
        # print("Hello {}! \nLet's play a game of RPS!".format(name))
        # print()
        # print('You start with 3 lives.')

        # while self.game_on():
        #     machine_choice = random.choice(choices)
        #     print('What are you choosing? These are your choices:')
        #     for i in names:
        #         print("- " + i)
        #     print()
        #     choice = input("- ")
        #     if choice in names:
        #         user_roll = Roll(choice)
        #         if user_roll.defeat(machine_choice) == "WIN":
        #             print("Machine's choice was {}: {} WINS!"
        #                   .format(machine_choice, user_roll))
        #         elif user_roll.defeat(machine_choice) == "LOSE":
        #             print("Machine's choice was {}: {} WINS!"
        #                   .format(machine_choice, machine_choice))
        #         else:
        #             print("TIED!")
        #     else:
        #         print('These are your choices:')
        #         for i in choices:
        #             print("- " + str(i))
        #             print()
        #     print()
        #     print('Lives: {}'.format(self.lives))

        # print('You have lost all your lifes! Come play other time!')
