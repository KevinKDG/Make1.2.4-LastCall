#!/usr/bin/env python
"""
Geeft informatie weer over de pinstatus van de RPi
"""


#               IMPORTS               #
import subprocess

#          AUTHOR INFORMATION         #

#        _____
#      .'     `.
#     /  .-=-.  \   \ __
#     | (  C\ \  \_.'')
#     _\  `--' |,'   _/
#    /__`.____.'__.-' The coding snail~

__author__ = "Kevin Vervloet"
__email__ = "kevin.vervloet@student.kdg.be"
__status__ = "Finished"


#              MAIN CODE              #
def main():
    def main():
        try:
            a = input("""Do you want to look at your GPIO pins?
    [1] Yes
    [2] No\n""")
            if a == "1":
                print("calling the script. . .")
                subprocess.run('./pinstatus', shell=True)
            elif a == "2":
                print("goodbye")

        except NameError:
            print('oops something went wrong')


if __name__ == '__main__':    #run tests if called from command-line
    main()