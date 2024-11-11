'''

Fleet Class a car_fleet_mgr.py file-hoz

5. házi feladat

Készíts egy Fleet osztályt, amely kezeli a Car objektumokat:
    - Az osztály rendelkezzen egy listával, amelyben az autók találhatóak.
    - Tartalmazzon metódusokat Car objektumok hozzáadására és eltávolítására a flottába/flottából.
    - Tartalmazzon egy metódust, amely összesíti a flotta összes autójának összes kilométerét. 
    - jelenítsd meg az autók állapotát és a flotta összesítő adatait
'''

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../_0_helpers')))

from car import Car
from LoggerSettingsForHomeworks import LoggerSettingsForHomeworks


class Fleet:
    """ Fleet class to manage a collection of Car objects """

    # class level logger
    log_file_path = os.path.join(os.path.dirname(__file__), 'logs', 'fleet_log.log')
    logger = LoggerSettingsForHomeworks(log_file_path).get_logger()

    def __init__(self):
        self.cars = []           # list to store Car objects

    def add_car(self, car:Car):
        """ Adds a Car object to the fleet """
        self.cars.append(car)
        self.logger.info(f"{car.id} added to fleet: {car.brand} {car.modell}")
        
    def remove_car(self, car:Car):
        """ Removes a Car object from the fleet """

        if car in self.cars:
            self.cars.remove(car)
            self.logger.info(f"Car removed from fleet: {car.brand} {car.modell}")
        else:
            self.logger.warning(f"Car not found in fleet: {car.brand}")

    def total_mileage(self):
        """ Calculates the total mileage of all cars in the fleet """

        total = sum(car.mileage for car in self.cars)

        self.logger.info(f"Total mileage of fleet: {total} km.")
        return total

    def show_fleet(self):
        """ Displays the state of each car in the fleet """   
        for car in self.cars:
            print(f"{car.id}: {car.brand} {car.modell}, Year: {car.year}, Mileage: {car.mileage}, Fuel Level: {car.fuel_level}") 