class Car:
    car_count = 0
    def __init__(self, brand: str, model: str, construction_year:int):
        self.brand = brand
        self.model = model
        self.construction_year = construction_year
        self.mileage = 0
        self.fuel_level = 100
        Car.car_count +=1

    def __str__(self):
        return f"{self.brand} {self.model} ({self.construction_year})"

    def drive(self, distance: float):
        average_usage = 0.1 #mert a kiinduló 100 ->%
        if  distance <=0:
            raise ValueError("Distance should be a positive number!")
        try:
            fuel_used = distance*average_usage
            max_distance=self.fuel_level/average_usage
            if fuel_used <= self.fuel_level:
               self.fuel_level -= fuel_used
               self.mileage +=distance
               max_distance-= self.mileage
               print(f"{self} drove: {distance} km - New mileage: {self.mileage} km - Fuel level:{self.fuel_level}%")
            else: 
                print(f"You have fuel only for {max_distance} km.")
        except ValueError as e:
            print(f"Value error {e}")
        except TypeError as e:
            print(f"Type error: {e}")

    def refuel(self,refilling_input:float):
        if  refilling_input <=0:
            raise ValueError("Fuel intake should be a positive number!")
        try:
            max_fuel_intake = 100 - self.fuel_level
            if max_fuel_intake  >= refilling_input:
               self.fuel_level += refilling_input
               print(f"New fuel level is {round(self.fuel_level,2)}% for car: {self}.")
            else: 
                print(f"You can fill only  {max_fuel_intake}% for car: {self}.")
        except ValueError as e:
            print(f"Value error {e}")
        except TypeError as e:
            print(f"Type error: {e}")

class Fleet:
    def __init__(self, name:str):
        self.name = name
        self.car_list = []

    def add_cars(self, car: Car):
        self.car_list.append(car)
        print(f"Added: {car}")

    def remove_cars(self, car: Car):
        self.car_list.remove(car)
        print(f"Removed: {car}")

    def total_mileage(self):
        total_miles=sum(car.mileage for car in self.car_list)
        print(f"Total miles for {self.name}: {total_miles} km")

    def listing_cars(self):
        if self.car_list:
            print(f"You have following cars in {self.name}: ")
            for number, car in enumerate(self.car_list, 1):
                print(f"\t{number}. {car}")
        else:
            print("This fleet is empty.")

car_1=Car("Hyunday", "i10", 2015)
car_2=Car("Kia", "Carens", 2016)
car_3=Car("Toyota", "XYZ", 2024)

fleet_1=Fleet("Céges flotta")
fleet_1.add_cars(car_1)
fleet_1.add_cars(car_2)
fleet_1.add_cars(car_3)

fleet_1.listing_cars()

car_1.drive(50)
car_1.refuel(2)

car_2.drive(70)

fleet_1.total_mileage()

fleet_1.remove_cars(car_2)
fleet_1.listing_cars()


