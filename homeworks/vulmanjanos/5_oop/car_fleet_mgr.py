# car class creation. self and basics creation
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0
        self.fuel_level = 100
# negativ km consumption is not an option
    def drive(self, driven_kilometers):
        if driven_kilometers < 0:
            print("Driven kilometers cannot be negative.")
            return
# fuel consumptions and rules
    def drive(self, driven_kilometers):
        fuel_consumption_calculator = driven_kilometers * 0.1
        if fuel_consumption_calculator <= self.fuel_level:
            self.mileage += driven_kilometers
            self.fuel_level -= driven_kilometers
        else:
            print("Not sufficient fuel amount to drive the desired distance.")
    def refuel(self, refill):
        if refill <= 0:
            print("Refill amount must be positive.")
            return
# fuel refilling and message
    def refuel(self, refill):
        if self.fuel_level + refill <= 100:
            self.fuel_level += refill
        else:
            self.fuel_level = 100
        print(f"Car has been refueled to {self.fuel_level}%")
   # Car fleet creation task. Self and element creation     
class Fleet:
    def __init__(self):
        self.skodacars = []

    def add_car(self, car):
        self.skodacars.append(car)
# check whether the car in the fleet
    def remove_car(self, car):
        if car in self.skodacars:
            self.skodacars.remove(car)
        else:
            print("Car is not in the fleet.")

    def total_mileage(self):
        return sum(car.mileage for car in self.skodacars)

# Creation of fleet
car1 = Car("Skoda", "Karoq", 2020)
car2 = Car("Skoda", "Kodiaq", 2021)
car3 = Car("Skoda", "Enyaq", 2022)
car4 = Car("Skoda", "Superb", 2023)

fleet = Fleet()
fleet.add_car(car1)
fleet.add_car(car2)
fleet.add_car(car3)
fleet.add_car(car4)

# Driving and refueling
car1.drive(310)
car1.refuel(270)
car2.drive(130)
car2.refuel(200)
car3.drive(150)
car3.refuel(175)
car4.refuel(350)

# Cars' condition
for car in fleet.skodacars:
    print(f"{car.brand} {car.model} ({car.year}) - Mileage: {car.mileage} km, Fuel Level: {car.fuel_level}%")

# Summary of fleet
print(f"Total mileage of the fleet: {fleet.total_mileage()} km")