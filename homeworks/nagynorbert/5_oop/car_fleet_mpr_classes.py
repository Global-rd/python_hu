# Homework 5. Nagy Norbert

class OutOfFuelError(Exception):
    """Fuel is not enough for the defined distance."""
    pass

class TooMuchFuelError(Exception):
    """Fuel is too much."""
    pass

class InvalidFuelError(Exception):
    """Amount of fuel is invalid."""
    pass

class CarDefineError(Exception):
    """Number of parameters for defining a car is not met with specification."""
    pass

class UserDefineError(Exception):
    """Number of how many cars should manipulate is incorrect."""
    pass

class Car:
    def __init__(self,brand:str,model:str,year:int,mileage:int = 0,fuel_level:int = 100):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage
        self.fuel_level = fuel_level
    
    def __str__(self):
        return f"Brand:{self.brand} -- Model:{self.model} -- Year:{self.year} -- Mileage:{self.mileage} -- Fuel_level:{self.fuel_level}"

    def drive(self,km:float):
        fuel_consumption = 0.1 * km
        if fuel_consumption > self.fuel_level:
            raise OutOfFuelError("Fuel is not enough in car.")
        self.mileage += km
        print(f"Mileage now: {self.mileage}")
        self.fuel_level -= fuel_consumption
        return True

    def refuel(self,fuel_amount:float):
        if fuel_amount < 0:
            raise InvalidFuelError("Invalid amount of fuel.")
        fuel_can_add = self.fuel_level + fuel_amount
        if fuel_can_add > 100:
            raise TooMuchFuelError("The amount of refuel is too much.")
        self.fuel_level += fuel_amount
        return True
    
    def __eq__(self,other):
        if self.brand == other.brand and self.model == other.model and self.year == other.year:
            return True
        return False
    
class Fleet:

    def __init__(self,name:str):
        self.name = name
        self.cars_in_fleet = []
        self.number_of_cars = 0

    def __str__(self):
        return f"{self.name}"

    def add_car_to_fleet(self,car:Car):
        self.cars_in_fleet.append(car)
        self.number_of_cars += 1

    def remove_car_from_fleet(self,car_remove:Car):
        self.cars_in_fleet.remove(car_remove)
        
    def summarize_miles_in_whole_fleet(self):
        sum_miles = 0
        for car in self.cars_in_fleet:
            sum_miles += car.mileage
        return sum_miles
    
    def print_whole_fleet(self):
        print(f"{self.name} contains following cars:")
        for car in self.cars_in_fleet:
            print(car)