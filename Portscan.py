#!/usr/bin/env python
"""
Heeft de mogelijkheid om enkele poorten te scannen.
"""


#               IMPORTS               #
import socket

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

#              VARIABLES              #
ip = '192.168.1.29'
port_list = [139, 80, 100, 125, 303, 5001]


#              MAIN CODE              #
def main():
    for port in port_list:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        results = s.connect_ex((ip, port))

        if results == 0:
            print('--------------------------')
            print('Port', port, 'is open')
            print('--------------------------')
        else:
            print('Port', port, 'is closed')


if __name__ == '__main__':    #run tests if called from command-line
    main()