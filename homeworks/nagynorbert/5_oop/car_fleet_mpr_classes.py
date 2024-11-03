# Homework 5. Nagy Norbert

class OutOfFuelError(Exception):
    """Fuel is not enough for the defined distance."""
    pass

class TooMuchFuelError(Exception):
    """Fuel is too much."""
    pass

class CarDefineError(Exception):
    """Number of parameters for defining a car is not met with specification."""
    pass

class UserDefineError(Exception):
    """Number of how many cars should manipulate is incorrect."""
    pass

class Car:
    def __init__(self,brand:str,model:str,year:int):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0
        self.fuel_level = 100
    
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
        fuel_can_add = self.fuel_level + fuel_amount
        if fuel_can_add > 100:
            raise TooMuchFuelError("The amount of refuel is too much.")
        self.fuel_level += fuel_amount
        return True
    
class Fleet:
    cars_in_fleet = []
    number_of_cars = 0

    def __init__(self,name:str):
        self.name = name

    def __str__(self):
        return f"{self.name}"

    def add_car_to_fleet(self,car:Car):
        self.cars_in_fleet.append(car)
        self.number_of_cars += 1 

    def cars_equal(self,car1:Car,car2:Car):
        if car1.brand == car2.brand and car1.model == car2.model and car1.year == car2.year:
            return True
        return False

    def remove_car_from_fleet(self,car_remove:Car):
        for idx,car in enumerate(self.cars_in_fleet):
            if self.cars_equal(car,car_remove):
                self.cars_in_fleet.pop(idx)
                self.number_of_cars -= 1
                return True
        return False
        

    def summarize_miles_in_whole_fleet(self):
        sum_miles = 0
        for car in self.cars_in_fleet:
            sum_miles += car.mileage
        return sum_miles
    
    def print_whole_fleet(self):
        print(f"{self.name} contains following cars:")
        for car in self.cars_in_fleet:
            print(car)