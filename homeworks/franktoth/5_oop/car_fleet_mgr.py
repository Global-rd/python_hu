#Creating Car class with the given attributes and methods

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0
        self.fuel_level = 100

    def drive(self, distance):
        if distance < 0:
            print(f"Error: Distance cannot be negative.")
            return

        fuel_consumption = distance * 0.1
        if fuel_consumption <= self.fuel_level:
            self.mileage += distance
            self.fuel_level -= fuel_consumption
            print(f"Car {self.brand} {self.model} drove {distance} km.")
        else:
            possible_distance = self.fuel_level / 0.1
            self.mileage += possible_distance
            self.fuel_level = 0
            print(f"Car {self.brand} {self.model} drove {possible_distance} km and ran out of fuel.")

    def refuel(self, amount):
        if amount < 0:
            print("Error: Fuel amount cannot be negative.")
            return
        self.fuel_level = min(self.fuel_level + amount, 100)
        print(f"Car {self.brand} {self.model} refueled. Current fuel level: {self.fuel_level}%")

#Creating Fleet class with the given methods

class Fleet:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def remove_car(self, brand, model):
        for car in self.cars:
            if car.brand == brand and car.model == model:
                self.cars.remove(car)
                print(f"Car {brand} {model} removed from the fleet.")
                return  # Exit after successful removal
        print(f"Error: Car {brand} {model} not found in the fleet.")

    def total_mileage(self):
        total_mileage = 0
        for car in self.cars:
            total_mileage += car.mileage
        return total_mileage

    def display_fleet(self):
        for car in self.cars:
            print(f"Brand: {car.brand}, Model: {car.model}, Year: {car.year}, Mileage: {car.mileage} km, Fuel Level: {car.fuel_level}%")
        print(f"Total Fleet Mileage: {self.total_mileage()} km")


# Create car sample objects
car1 = Car("Audi", "A6", 2023)
car2 = Car("Honda", "Civic", 2022)
car3 = Car("Ford", "Mustang", 2021)
car4 = Car("Opel", "Astra", 2018)

# Create a fleet
fleet = Fleet()
fleet.add_car(car1)
fleet.add_car(car2)
fleet.add_car(car3)
fleet.add_car(car4)

# Drive the cars
car1.drive(100)
car2.drive(50)
car3.drive(200)
car4.drive(1300)

#Remove the cars from the fleet
fleet.remove_car("Opel","Astra")
fleet.remove_car("Tesla", "Model3")

# Refuel car1
car1.refuel(30)
car4.refuel(50)

# Display fleet information
fleet.display_fleet()