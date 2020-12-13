#!/usr/bin/env python
"""
It's a calculator...
"""


#               IMPORTS               #
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
def error():
    print('this is not a valid number, Please try again')              # print this message if the input isn't a number
    time.sleep(0.5)
    main()


def addition(number_1, number_2):
    """addition of the two numbers"""

    print(number_1, "+", number_2, "is", number_1 + number_2)                 # Do the calculation
    time.sleep(0.5)                                                           # wait a bit . . .


def subtraction(number_1, number_2):
    """subtraction of the two numbers"""

    print(number_1, "-", number_2, "is", number_1 - number_2)
    time.sleep(0.5)


def multiplication(number_1, number_2):
    """multiplication of the two numbers"""

    print(number_1, "*", number_2, "is", number_1 * number_2)
    time.sleep(0.5)


def division(number_1, number_2):
    """division of the two numbers"""

    print(number_1, "/", number_2, "is", number_1 / number_2)
    time.sleep(0.5)


def main():

    try:
        number_1 = float(input("Pick a number: "))  # Input, pick your first number
        number_2 = float(input("Pick another number: "))  # Input, it lets you pick a second number

        what = input('''
---------------------------------        
|   What would you like to do?  |   
|-------------------------------|       
| [1] for addition (+)          |
| [2] for subtraction (-)       |
| [3] for multiplication (*)    |
| [4] for division (/)          |
---------------------------------\n''')
        if what == "1":
            addition(number_1, number_2)

        elif what == '2':
            subtraction(number_1, number_2)

        elif what == '3':
            multiplication(number_1, number_2)

        elif what == '4':
            division(number_1, number_2)

        elif what != "+" or "-" or "*" or "/":
            print("Thats not a valid mathematical function")
            main()

    except ValueError:
        error()


if __name__ == '__main__':    # run tests if called from command-line
    main()