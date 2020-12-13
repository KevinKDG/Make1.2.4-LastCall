#!/usr/bin/env python
"""
Gives information about the local computer
"""


#               IMPORTS               #
import platform

#          AUTHOR INFORMATION         #

#        _____
#      .'     `.
#     /  .-=-.  \   \ __
#     | (  C\ \  \_.'')
#     _\  `--' |,'   _/
#    /__`.____.'__.-' The coding snail~

__author__ = "Kevin Vervloet"
__email__ = "kevin.vervloet@student.kdg.be"
__status__ = "Development"




#              MAIN CODE              #
def sys_information():
    print("=====================System Information========================")
    my_system = platform.uname()
    print(f"System: {my_system.system}")
    print(f"Node Name: {my_system.node}")
    print(f"Release: {my_system.release}")
    print(f"Version: {my_system.version}")
    print(f"Machine: {my_system.machine}")
    print(f"Processor: {my_system.processor}")
    print("===============================================================")
    print("")


if __name__ == '__main__':    # run tests if called from command-line
    sys_information()