class Car:
    car_count = 0

    def __init__(self, brand: str, model: str, production_year: int, mileage_standing: int = 0, fuel_level: float = 100):
        self.brand = brand
        self.model = model
        self._production_year = production_year
        self._mileage_standing = mileage_standing
        self.fuel_level = fuel_level
        Car.car_count +=1

    def drive(self, kilometer: float):
        if kilometer <= 0:
            raise ValueError(f"Driving negative or zero distance is impossible with {self.brand} {self.model} car. Please enter a positive number.")
        
        fuel_needed = kilometer * 0.1
        if fuel_needed <= self.fuel_level:
            self._mileage_standing += kilometer
            self.fuel_level -= fuel_needed
            print(f"You drove {kilometer} kilometer with {self.brand} {self.model} and the tank of your car dropped by {fuel_needed}%. ")
        else:    
            max_distance = self.fuel_level / 0.1
            print(f"You can only drive {max_distance} with the {self.brand} {self.model}. Please find a gas station and refuel the tank or plan a shorter route.")

    def refuel(self, amount: float):
        if amount <= 0:
            print("Amount should be a positive number")
        elif self.fuel_level + amount > 100:
            max_fuel = 100 - self.fuel_level
            print(f"You entered too much fuel into {self.brand} {self.model}. Maximum percentage to fill the tank full is {max_fuel}. Current fuel level: {self.fuel_level} ")  
            return
        else:
            self.fuel_level += amount
            print(f"The tank of the {self.brand} {self.model} was fueled by {amount}%. Current fuel level: {self.fuel_level}%.")

    def __str__(self):
        return f"{self.brand} {self.model} - {self._production_year}"
    
    def get_mileage(self):
        return self._mileage_standing

class Fleet:
    def __init__(self):
        self.cars = []

    def remove_car(self, car: Car):
        if car in self.cars:
            self.cars.remove(car)
            print(f"The {car.brand} {car.model} is removed from the fleet.")
        else:
           raise ValueError(f"The {car.brand} {car.model} is not part of the fleet.") 


    def add_car(self, car: Car):
        self.cars.append(car)   

    def total_mileage(self):
        return sum(car._mileage_standing for car in self.cars)
    
    def car_list(self):
        if self.cars:
            for number, car in enumerate(self.cars, 1):
                print(f"{number}. {car}")
        else:
            print("The fleet is empty.")

#Create car objects
car1 = Car(brand="Toyota", model="Avensis", production_year=2004, mileage_standing=350000, fuel_level=100)
car2 = Car(brand="Audi", model="RS7", production_year=2017, mileage_standing=56000, fuel_level=78)
car3 = Car(brand="Ford", model="Focus", production_year=2010, mileage_standing=280000, fuel_level=45)
car4 = Car(brand="Porche", model="Panamera", production_year=2021, mileage_standing=18000, fuel_level=67)

#Create fleed and add cars
fleet = Fleet()
fleet.add_car(car1)
fleet.add_car(car2)
fleet.add_car(car3)
fleet.add_car(car4)

#Use drive methods on cars
car1.drive(10)
car2.drive(150)
car3.drive(342)
car4.drive(700)

#Use refuel methods on cars
car1.refuel(10)
car2.refuel(12)
car3.refuel(50)
car4.refuel(13)

#Use remove method on fleet
fleet.remove_car(car3)

#Use total_mileage method on fleet
fleet.total_mileage()

#List the cars in the fleet
fleet.car_list()

print(f"There {'is' if len(fleet.cars) == 1 else 'are'} {len(fleet.cars)} car{'s' if len(fleet.cars) != 1 else ''} in the fleet.")
