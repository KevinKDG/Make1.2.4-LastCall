#!/usr/bin/env python
"""
Hoofdmenu
"""


#               IMPORTS               #
import sys
import time
from datetime import datetime

#            IMPORTS SCRIPTS          #
import IP
import password
import rekentoestel
import system
import update
import InstallSoftware
import Pinstatus
import Portscan

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
__status__ = "Development"

#              VARIABLES              #

time_now = datetime.now()
current_time = time_now.strftime("%H:%M:%S")


#              MAIN CODE              #
def homepage():

    print("[", current_time, "]", " ====Toolscript===")     # Print the time & a title

    greetings = (input("""                                  
--------------------------------------------------------------------------------------------------    
| [1] Call calculator             [6] Portscanning                                                |
| [2] Call password generator     [7] Install RPi software: Apache, MariaDB, PHP                 |
| [3] Show IP                     [8] GPIO pin state                                              |
| [4] system info                 [9] Exit                                                        |
| [5] Update & upgrade RPi                                                                        |
--------------------------------------------------------------------------------------------------\n"""))

    if greetings == "1":
        rekentoestel.main()         # Run the calculator script
        time.sleep(1)
        print("")
        homepage()                  # Go back to the main menu

    elif greetings == "2":
        password.main()
        time.sleep(1)
        print("")
        homepage()

    elif greetings == "3":
        IP.get_Host_name_IP()
        time.sleep(1)
        print("")
        homepage()

    elif greetings == "4":
        system.sys_information()
        time.sleep(1)
        print("")
        homepage()

    elif greetings == "5":
        update.main()
        print("")
        homepage()

    elif greetings == "6":
        Portscan.main()
        print("")
        homepage()

    elif greetings == "7":
        InstallSoftware.main()
        print("")
        homepage()

    elif greetings == "8":
        Pinstatus.main()
        print("")
        homepage()

    elif greetings == "9":
        print("See you next time!")
        sys.exit(0)

    elif greetings != "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9": # error message
        print("Error! Try again")
        time.sleep(1)
        print("")
        print("")
        homepage()


if __name__ == '__main__':    # run tests if called from command-line
    homepage()