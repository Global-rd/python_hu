class DuplicateLicensePlateError(Exception):
    """Raised when a car with the same license plate number already exists."""
    pass

class Car:
    registered_license_plates = set()

    def __init__(self, brand, model, year, license_plate_number):
        try:
            if license_plate_number in Car.registered_license_plates:
                raise DuplicateLicensePlateError(f"License plate '{license_plate_number}' already exists.")
            self.brand = brand
            self.model = model
            self.year = year
            self.mileage = 0
            self.fuel_level = 100
            self.license_plate_number = license_plate_number
            Car.registered_license_plates.add(license_plate_number)
        except DuplicateLicensePlateError as e:
            print(e)

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

class Fleet:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        try:
            self.cars.append(car)
            print(f"Car {car.brand} {car.model} with {car.license_plate_number} LPN added to the fleet.")
        except DuplicateLicensePlateError as e:
            print(e)

    def remove_car(self, license_plate_number):
        for car in self.cars:
            if car.license_plate_number == license_plate_number:
                self.cars.remove(car)
                print(f"Car with LPN {license_plate_number} removed from the fleet.")
                return
        print(f"Error: Car with LPN {license_plate_number} not found in the fleet.")

    def total_mileage(self):
        total_mileage = 0
        for car in self.cars:
            total_mileage += car.mileage
        return total_mileage

    def display_fleet(self):
        for car in self.cars:
            print(f"Brand: {car.brand}, Model: {car.model}, Year: {car.year}, License Plate: {car.license_plate_number}, Mileage: {car.mileage} km, Fuel Level: {car.fuel_level}%")
        print(f"Total Fleet Mileage: {self.total_mileage()} km")

# Create car sample objects (with license plate numbers)

car1 = Car("Audi", "A6", 2023, "12345")
car2 = Car("Honda", "Civic", 2022, "56787")
car3 = Car("Ford", "Mustang", 2021, "65327")
car4 = Car("Opel", "Astra", 2018, "12345")  # Duplicate license plate
car5 = Car("Opel", "Astra", 2018, "98765")

# Create a fleet
fleet = Fleet()
fleet.add_car(car1)
fleet.add_car(car2)
fleet.add_car(car3)
fleet.add_car(car5)

# Drive the cars
car1.drive(100)
car2.drive(50)
car3.drive(200)
car5.drive(1300)

#Remove the cars from the fleet
fleet.remove_car("12345")
fleet.remove_car("43434")

# Refuel car1
car1.refuel(30)
car5.refuel(50)

# Display fleet information
fleet.display_fleet()