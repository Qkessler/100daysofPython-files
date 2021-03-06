import random
import sys
import logbook


app_log = logbook.Logger('App')

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
        app_log.trace("Initializing setup and gameloop.")
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
        name.strip()
        while name == "":
            name = input("- ").strip()
            if name == "":
                app_log.error("User chose a blank name")
                raise ValueError("ERROR: Name cannot be blank!")
            
        app_log.trace("User's name: {}".format(name))
        print("Hey {}! Welcome to the rps game!".format(name))
        print('You start with 3 lives.')

        app_log.trace("Entering main loop.")
        number_choice = 1
        while self.game_on():
            machine_choice = random.choice(choices)
            print('What are you choosing? r, p, s: ')
            choice = input("- ")
            app_log.trace("{} user's choice is {}.".format(number_choice, choice))

            if choice == 'r':
                print('You have chosen Rock!')
                print("The machine's choice was {}!".format(machine_choice))
                if machine_choice == "Rock":
                    result = 'Tied!'
                elif machine_choice == 'Paper':
                    result = 'Paper > Rock! You lose!'
                    self.decrement_lives()
                else:
                    result = 'Scissors < Rock! You win!'
            elif choice == 'p':
                print('You have chosen Paper!')
                print("The machine's choice was {}!".format(machine_choice))
                if machine_choice == "Paper":
                    result = 'Tied!'
                elif machine_choice == 'Rock':
                    result = 'Paper > Rock! You win!'
                else:
                    result = 'Scissors > Paper! You lose!'
                    self.decrement_lives()
            elif choice == 's':
                print('You have chosen Scissors!')
                print("The machine's choice was {}!".format(machine_choice))
                if machine_choice == "Scissors":
                    result = 'Tied!'
                elif machine_choice == 'Paper':
                    result = 'Paper < Scissors! You win!'
                else:
                    result = 'Scissors < Rock! You lose!'
                    self.decrement_lives()
            else:
                app_log.warn("User chose a non supported choice: {}".format(choice))
                print('Your 3 choices are: r, s, p!')
            app_log.trace("{} machine's choice is {}.".format(number_choice, machine_choice))
            print()
            print('Lives: {}'.format(self.lives))
            number_choice += 1

        app_log.trace("Game ended")
        print('You have lost all your lifes! Come play other time!')
