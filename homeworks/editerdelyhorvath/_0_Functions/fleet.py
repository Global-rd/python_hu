'''

Fleet Class a car_fleet_mgr.py file-hoz

5. házi feladat

Készíts egy Fleet osztályt, amely kezeli a Car objektumokat:
    - Az osztály rendelkezzen egy listával, amelyben az autók találhatóak.
    - Tartalmazzon metódusokat Car objektumok hozzáadására és eltávolítására a flottába/flottából.
    - Tartalmazzon egy metódust, amely összesíti a flotta összes autójának összes kilométerét. 
    - jelenítsd meg az autók állapotát és a flotta összesítő adatait
'''

from car import Car

class Fleet:
    """ Fleet class to manage a collection of Car objects """

    def __init__(self, logger=None):
        self.cars = []           # list to store Car objects
        self.logger = logger

    def add_car(self, car:Car):
        """ Adds a Car object to the fleet """
        self.cars.append(car)

        if self.logger:
            self.logger.info(f"{car.name} added to fleet: {car.brandbrand} {car.modell}")
        
    def remove_car(self, car:Car):
        """ Removes a Car object from the fleet """

        if car in self.cars:
            self.cars.remove(car)
            if self.logger:
                self.logger.info(f"Car removed from fleet: {car.brandbrand} {car.modell}")
        else:
            if self.logger:
                self.logger.warning(f"Car not found in fleet: {car.brandbrand}")

    def total_mileage(self):
        """ Calculates the total mileage of all cars in the fleet """

        total = sum(car.mileage for car in self.cars)

        if self.logger:
            self.logger.info(f"Total mileage of fleet: {total} km.")
        return total

    def show_fleet(self):
        """ Displays the state of each car in the fleet """   
        for car in self.cars:
            print(f"{car.name}: {car.brandbrand} {car.modell}, Year: {car.year}, Mileage: {car.mileage}, Fuel Level: {car.fuel_level}") 