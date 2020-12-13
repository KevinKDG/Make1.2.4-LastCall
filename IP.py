#!/usr/bin/env python
"""
Dit scriptje zal meteen jouw lokale IP adres vinden
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


#              MAIN CODE              #
def get_Host_name_IP():
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)

        print("Host IP : ", host_ip)
    except:
        print("Unable to get Hostname and IP")


if __name__ == '__main__':    #run tests if called from command-line
    get_Host_name_IP()