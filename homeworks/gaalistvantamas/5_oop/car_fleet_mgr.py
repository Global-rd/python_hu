"""
Author: Gaál István Tamás
Task: Homework-5
"""

class Car:

    FUEL_USAGE = 0.1
    
    def __init__(self, brand, model, year, mileage = 0, fuel_level = 100.0):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage
        self.fuel_level = fuel_level

    def drive(self, road_length_in_kilometres):
        if road_length_in_kilometres < 1:
            print("Please give a bigger number than 0!")
        
        elif not road_length_in_kilometres > int(self.fuel_level / self.FUEL_USAGE):
            self.mileage += road_length_in_kilometres
            self.fuel_level -= road_length_in_kilometres * self.FUEL_USAGE
            print(f"You drove {road_length_in_kilometres} km and the fuel usage of the trip was {round(100 - self.fuel_level)}%!")

        else:
            print("There is no enough fuel in the car!")
            print(f"You can drive maximum: {self.fuel_level / self.FUEL_USAGE} km!")

    def refuel(self, refuel_percents):
        if refuel_percents < 1:
            print("Please give a bigger number than 0!")
        
        elif refuel_percents > (100.0 - self.fuel_level):
            print(f"You can refuel maximum {round(100 - self.fuel_level)}%!")
        
        else:
            self.fuel_level += refuel_percents

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Mileage: {self.mileage}")
        print(f"Fuel level: {self.fuel_level}\n")

class Fleet:
    def __init__(self,) -> None:
        self.cars = []
    
    def add_car(self, car_to_be_added):
        self.cars.append(car_to_be_added)
        print("This car has to be added the fleet:") 
        print(f"{car_to_be_added.brand} {car_to_be_added.model} {car_to_be_added.year}\n")

    def remove_car(self, car_to_be_removed):
        self.cars.remove(car_to_be_removed)
        print(f"This car has to be removed the fleet:") 
        print(f"{car_to_be_removed.brand} {car_to_be_removed.model} {car_to_be_removed.year}\n")
    
    def all_kilometers(self):
        all_km = 0
        for car in self.cars:
            all_km += car.mileage
        print(f"All kilometers of the fleet: {all_km} km!")

    def car_info(self):
        print("\nInfo of the cars in the fleet:")
        for car in self.cars:
            car.display_info()
    
    def fleet_info(self):
        print(f"Number of cars: {len(self.cars)}")

car_fleet = Fleet()

car_1 =Car("Ford", "Focus", 2002)
car_2 =Car("Ford", "Mondeo", 2021)
car_3 =Car("Lada", "Samara", 1994)


car_fleet.add_car(car_1)
car_fleet.add_car(car_2)
car_fleet.add_car(car_3)

car_1.drive(50)
car_1.display_info()
car_1.drive(5000)
car_1.display_info()
car_1.drive(-10)
car_1.display_info()

car_1.refuel(10)
car_1.display_info()
car_1.refuel(-10)
car_1.display_info()

car_2.drive(200)
car_2.display_info()

car_fleet.remove_car(car_3)

car_fleet.all_kilometers()
car_fleet.car_info()
car_fleet.fleet_info()

