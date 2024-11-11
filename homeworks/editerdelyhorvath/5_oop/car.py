'''

Car Class a car_fleet_mgr.py file-hoz

5. házi feladat

Készíts egy Car osztályt, amely rendelkezik a következő tulajdonságokkal:
    - Márka (brand)
    - Modell (model)
    - Gyártási év (year)
    - Kilométeróra állása (mileage), induló értéke 0.
    - Üzemanyag-szint (fuel_level), induló értéke 100 (százalékban).

Az osztály tartalmazza a következő metódusokat:
    - Egy konstruktor, amely beállítja a fenti attribútumokat.
    - Egy drive() metódus, amely adott számú kilométerrel növeli a kilométeróra állását, 
    és csökkenti az üzemanyag-szintet (tételezzük fel, hogy 0.1% üzemanyag fogy megtett kilométerenként). 
    A drive() metódus csak annyit km-et engedjen vezetni, amennyire elegendő üzemanyag van.
    - Egy refuel() metódus, amely feltölti az üzemanyag-szintet egy adott mennyiséggel. Figyelj a limitekre.

'''
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../_0_helpers')))

from LoggerSettingsForHomeworks import LoggerSettingsForHomeworks
from exception_handling_to_classes import InvalidAmountError


####################  Car Class  #################### 

class Car:
    """ Create a car, drive a car and refuel a car"""

    # class level logger
    log_file_path = os.path.join(os.path.dirname(__file__), 'logs', 'fleet_log.log')
    logger = LoggerSettingsForHomeworks(log_file_path).get_logger()

    car_count = 0
    
    def __init__(self, brand:str, modell:str, year:int, mileage:float = 0, fuel_level:float = 100):

        Car.car_count += 1
        self.id = Car.car_count
        self.brand = brand
        self.modell = modell
        self.year = year
        self.mileage = mileage
        self.fuel_level = fuel_level
    



    def drive(self, distance:float):

        fuel_needed = distance * 0.1

        if self.fuel_level < fuel_needed:
            error_message = f"For {self.id} there is not enough fuel to drive {distance} km."
            raise InvalidAmountError(error_message)
        
        self.mileage += distance
        self.fuel_level -= fuel_needed
        self.logger.info(f"{self.id} drove {distance} km. New mileage: {self.mileage}, fuel level: {self.fuel_level}.")

    def refuel(self, amount:float):

        if self.fuel_level + amount > 100:
            fuel_to_max = 100 - self.fuel_level
            error_message = f"For {self.id}, You have entered too much fuel, the maximum missing amount: {fuel_to_max}."
            raise InvalidAmountError(error_message)

        self.fuel_level += amount
        self.logger.info(f"{self.id} refueled with {amount} units. New fuel level: {self.fuel_level}.")

    def __str__(self):
        return f"Car {self.id}: {self.brand} {self.modell}, Year: {self.year}, Mileage: {self.mileage}, Fuel Level: {self.fuel_level}"

        
            
            

        

