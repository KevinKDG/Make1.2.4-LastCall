#!/usr/bin/env python
"""
Will generate a random password
"""

#               IMPORTS               #

import random
import time

#          AUTHOR INFORMATION         #

#        _____
#      .'     `.
#     /  .-=-.  \   \ __
#     | (  C\ \  \_.'')
#     _\  `--' |,'   _/
#    /__`.____.'__.-' The coding snail~

__author__ = "Kevin Vervloet"
__email__ = "kevin.vervloet@student.kdg.be"
__Version__ = "(Code version)"
__status__ = "Finished"


#              VARIABLES              #

#              MAIN CODE              #


def high_security():
    """ High security password code"""

    print("==You picked high security==")
    time.sleep(0.5)
    lenght = int(input("How long do you want your password to be?: "))
    characters_high = list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*(){}[]<>,.')

    password_random_characters = [random.choice(characters_high) for i in range(lenght)]
    password = "".join(password_random_characters)
    print("This is your random password", password)


def medium_security():
    """ Medium security password code"""

    print("==You picked medium security==")
    time.sleep(0.5)
    lenght = int(input("How long do you want your password to be?: "))
    characters_medium = list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890')

    password_random_characters = [random.choice(characters_medium) for i in range(lenght)]
    password = "".join(password_random_characters)
    print("This is your random password", password)

def low_security():
    """ Low security password code"""

    print("==You picked low security==")
    time.sleep(0.5)
    lenght = int(input("How long do you want your password to be?: "))
    characters_low = list('abcdefghijklmnopqrstuvwxyz1234567890')

    password_random_characters = [random.choice(characters_low) for i in range(lenght)]  # picks random characters
    password = "".join(password_random_characters)
    print("This is your random password", password)


def main():

    what = input("""
---------------------------------------------------------------------    
|             How strong do you want your password to be?           |
|-------------------------------------------------------------------|
| [1] low (only small letters & numbers)                            |
| [2] medium (small letters, numbers & capital letters)             |
| [3] high (small letters, capital letters, numbers & symbols       |
---------------------------------------------------------------------\n """)   # Input question

    if what == "1":
        low_security()

    elif what == "2":
        medium_security()

    elif what == "3":
        high_security()

    elif what != "1" or "2" or "3":                         # if the input is wrong restart the program
        print("Not a valid option, please try again")
        time.sleep(0.5)
        main()


if __name__ == '__main__':  # run tests if called from command-line
    main()
