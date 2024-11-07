class Car:
    def __init__(self, brand: str, model: str, year: int):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0                    
        self.fuel_level = 100               

    def drive(self, kilometers):
        fuel_needed = kilometers * .1
        if self.fuel_level > fuel_needed:
            self.fuel_level -= fuel_needed
            self.mileage += kilometers
        else:
            print(f'Find a gas station.')

    def refuel(self, amount):
        if self.fuel_level + amount > 100:
            self.fuel_level = 100
        else:
            self.fuel_level += amount
            print(f"{self.brand} {self.model} refueled. Fuel level is now {self.fuel_level}%.")


class Fleet:
    def __init__(self, name):
        self.name = name
        self.cars = []  

    def add_cars(self, car):
        self.cars.append(car)

    def remove_car(self, car):
        if car in self.cars:
         self.cars.remove(car)

    def total_mileage(self):
        return sum(car.mileage for car in self.cars)
    
    def __str__(self):
        return f"Total performance of the fleet: {self.total_mileage()} km"


###############################################################################################################################
  
    car1 = Car("Audi", "Quattro", 1980)
    car2 = Car("Lamborghini", "Urus", 2024)
    car3 = Car("Seat", "Ibiza", 2018) 
    car4 = Car("Volkswagen", "Golf", 2015) 

    fleet = Fleet()

    fleet.add_cars(car1)
    fleet.add_cars(car2)
    fleet.add_cars(car3)
    fleet.add_cars(car4)

    car1.drive(kilometers = 10)
    car2.drive(kilometers = 250)
    car3.drive(kilometers = 526)
    car4.drive(kilometers  = 1111)

    car1.refuel(amount = 20)
    car2.refuel(amount = 56)
    car3.refuel(amount = 50)
    car4.refuel(amount = 65)

    print(f"Traveled road: {fleet.total_mileage()} km\n")


