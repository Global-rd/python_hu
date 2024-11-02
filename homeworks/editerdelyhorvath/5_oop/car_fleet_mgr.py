'''
5. házi feladat

Main

Flotta kezelő alkalmazás

Hozz létre néhány Car objektumot, add hozzá őket a flottához, 
hajts végre néhány műveletet (vezetés, tankolás),  
jelenítsd meg az autók állapotát és a flotta összesítő adatait.

'''

import sys
import os

from colorama import Fore, Style, init

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../_0_Functions')))

from car import Car
from exception_handling_to_classes import InvalidAmountError
from LoggerSettingsForHomeworks import LoggerSettingsForHomeworks
from fleet import Fleet
from terminal_clearer import clear_terminal   

# Initialising colorama to work on Windows
init(autoreset=True)

#################### LOGGER SETUP #################### 

# Define the current directory and log directory within the main file's location
current_dir = os.path.dirname(os.path.abspath(__file__))
log_dir = os.path.join(current_dir, 'logs')
log_file_path = os.path.join(log_dir, 'car_fleet_log.log')

# Ensure the log directory exists
os.makedirs(log_dir, exist_ok=True)

# Set up logging with logger_settings
logger_settings = LoggerSettingsForHomeworks(log_file_path)
logger = logger_settings.get_logger()        


#################### Main File #################### 

clear_terminal()

try:

    # create a fleet
    fleet1 = Fleet(logger=logger)

    # create some car objects
    car1 = Car(name="car1", brand="Ford", modell="S-max", year=2020, mileage=32542, fuel_level=100, logger=logger)
    car2 = Car(name="car2", brand="Ford", modell="Fiesta", year=2019, mileage=35430, fuel_level=80, logger=logger)
    car3 = Car(name="car3", brand="Toyota", modell="Corolla", year=2018, mileage=45000, fuel_level=90, logger=logger)

    # add cars to the fleet
    print(Fore.BLUE + "Cars added to the fleet: " + Style.RESET_ALL)
    fleet1.add_car(car1)
    fleet1.add_car(car2)
    fleet1.add_car(car3)

    # display fleet status
    print(Fore.BLUE + "\nFleet status before operations: " + Style.RESET_ALL)
    fleet1.show_fleet()

    # perform some operations
    print(Fore.BLUE + "\nPerformed operations: " + Style.RESET_ALL)
    try:
        car1.drive(150)
    except InvalidAmountError as e:
        print(e)

    try:
        car2.drive(230)
    except InvalidAmountError as e:
        print(e)

    try:
        car3.drive(1600)
    except InvalidAmountError as e:
        print(e)
        

    try:
        car1.refuel(50)
    except InvalidAmountError as e:
        print(e)

    try:
        car2.refuel(30)
    except InvalidAmountError as e:
        print(e)

    try:
        car3.refuel(10)
    except InvalidAmountError as e:
        print(e)
        

    # display fleet status 
    print(Fore.BLUE + "\nFleet status after operations: " + Style.RESET_ALL)
    fleet1.show_fleet()

    # Show total mileage of the fleet
    print(Fore.BLUE + f"\nFleet summary data:" + Style.RESET_ALL)
    total_mileage = fleet1.total_mileage()
    print()

except InvalidAmountError as e:
    print(e)