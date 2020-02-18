import random


class Roll():
    def __init__(self, name):
        self.name = name
        self.defeat = self.defeat()
        self.beDefeated = self.beDefeated()

    def defeat(self):
        if self.name == 'Rock':
            return 'Scissors'
        elif self.name == 'Paper':
            return 'Rock'
        elif self.name == 'Scissors':
            return 'Paper'
        else:
            print('The roll is not coded yet')

    def beDefeated(self):
        if self.name == 'Rock':                                                                                                                     
            return 'Paper'                                                                                                                       
        elif self.name == 'Paper':                                                                                                                  
            return 'Scissors'
        elif self.name == 'Scissors':                                                                                                               
            return 'Rock'
        else:
            print('The roll is not coded yet')

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
        choices = [
            Roll("Paper"), Roll("Rock"), Roll("Scissors")
             ]
        print('Welcome to the game of RPS!')
        print('What is your name?')
        name = input("- ")
        print("Hello {}! \nLet's play a game of RPS!".format(name))
        print()
        print('You start with 3 lives.')

        while self.game_on():
            machine_choice = random.choice(choices)
            print('What are you choosing? r, p, s: ')
            choice = input("- ")

            if choice == 'r':
                print('You have chosen Rock!')
                print("The machine's choice was {}!".format(machine_choice))
                if machine_choice == "Rock":
                    print('Tied!')
                elif machine_choice == 'Paper':
                    print('Paper > Rock! You lose!')
                    self.decrement_lives()
                else:
                    print('Scissors < Rock! You win!')
            elif choice == 'p':
                print('You have chosen Paper!')
                print("The machine's choice was {}!".format(machine_choice))
                if machine_choice == "Paper":
                    print('Tied!')
                elif machine_choice == 'Rock':
                    print('Paper > Rock! You win!')
                else:
                    print('Scissors > Paper! You lose!')
                    self.decrement_lives()
            elif choice == 's':
                print('You have chosen Scissors!')
                print("The machine's choice was {}!".format(machine_choice))
                if machine_choice == "Scissors":
                    print('Tied!')
                elif machine_choice == 'Paper':
                    print('Paper < Scissors! You win!')
                else:
                    print('Scissors < Rock! You lose!')
                    self.decrement_lives()
            else:
                print('Your 3 choices are: r, s, p!')
            print()
            print('Lives: {}'.format(self.lives))

        print('You have lost all your lifes! Come play other time!')
