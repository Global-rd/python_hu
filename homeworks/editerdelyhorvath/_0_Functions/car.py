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

from exception_handling_to_classes import InvalidAmountError

####################  Car Class  #################### 

class Car:
    """ Create a car, drive a car and refuel a car"""

    car_count = 0
    
    def __init__(self, name, brand:str, modell:str, year:int, mileage:float = 0, fuel_level:float = 100, logger=None):

        self.name = name
        self.brandbrand = brand
        self.modell = modell
        self.year = year
        self.mileage = mileage
        self.fuel_level = fuel_level
        self.logger = logger  

        Car.car_count += 1


    def drive(self, distance:float):

        fuel_needed = distance * 0.1

        if self.fuel_level < fuel_needed:
            error_message = f"For {self.name} there is not enough fuel to drive {distance} km."
            raise InvalidAmountError(error_message, logger=self.logger)
        
        self.mileage += distance
        self.fuel_level -= fuel_needed
        if self.logger:
            self.logger.info(f"{self.name} drove {distance} km. New mileage: {self.mileage}, fuel level: {self.fuel_level}.")


    def refuel(self, amount:float):

        if self.fuel_level + amount > 100:
            fuel_to_max = 100 - self.fuel_level
            error_message = f"For {self.name}, You have entered too much fuel, the maximum missing amount: {fuel_to_max}."
            raise InvalidAmountError(error_message, logger=self.logger)

        self.fuel_level += amount
        if self.logger:
            self.logger.info(f"{self.name} refueled with {amount} units. New fuel level: {self.fuel_level}.")

        
            
            

        

