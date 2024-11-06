class Car:
    def __init__(self, brand, model, year, mileage=0, fuel_level=100):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage
        self.fuel_level = fuel_level

    def drive(self, distance):                              # car fuel consumption calculation
        fuel_consumption = distance * 0.1
        if self.fuel_level > fuel_consumption:
            self.mileage += distance
            self.fuel_level -= fuel_consumption
            print(f"The {self.brand} {self.model} distance: {self.mileage},fuel level: {self.fuel_level}")
        else:
            print(f"The {self.brand} {self.model} does not have enough fuel for this range!")

    def refuel(self, fuel_amount):                          # Reload method
        if self.fuel_level + fuel_amount >= 100:
            self.fuel_level = 100
            print(f"The {self.brand} {self.model} is fully reloaded!")
        else:
            self.fuel_level += fuel_amount
            print(f"The {self.brand} {self.model} reloaded!")

class Fleet:
    def __init__(self):
        self.cars = []

    def add_car(self, car: Car):                          # Add car to the list - method
        self.cars.append(car)
        print(f"A car added to the fleet: {car.brand} {car.model}")

    def remove_car(self, car: Car):                       # Remove car to the list - method
        if car in self.cars:
            self.cars.remove(car)
            print(f"Removed {car.brand} {car.model} from the fleet.")
        else:
            print(f"The specified car is not in the fleet: {car.brand} {car.model}!")

    def total_run_km(self):                                # Summary of all kilometers traveled by the fleet
        total_run = sum(car.mileage for car in self.cars)
        print(f"Total mileage of the fleet: {total_run} km.")
        return total_run
    
    def fleet_condition(self):
        print("The condition of fleet cars:")
        for cars in fleet.cars:
            print(f"{cars.brand} {cars.model} {cars.mileage}km, {cars.fuel_level}%")
    
#------------------------------------------- Main program ----------------------------------

# -------------------------------------- Define cars in fleet -------------------------------
car_1 = Car("Opel", "Corsa", 2006)
car_2 = Car("Opel", "Astra", 2010)
car_3 = Car("Ford", "Focus", 2014)

# -------------------------------------- Creating Fleet -------------------------------------
fleet = Fleet()

fleet.add_car(car_1)
fleet.add_car(car_2)
fleet.add_car(car_3)

# -------------------------------------- Drive cars --------------------------------------
car_1.drive(125)
car_2.drive(258)
car_3.drive(1500)

# -------------------------------------- Refuel cars --------------------------------------
car_1.refuel(20)
car_2.refuel(20)
car_3.refuel(30)

# ------------------------------ the condition of the cars --------------------------------
fleet.fleet_condition()
# ------------------------------ Total milage of the fleet --------------------------------
fleet.total_run_km()

