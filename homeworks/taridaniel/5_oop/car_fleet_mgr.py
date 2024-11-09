class Car:
    def __init__(self, brand, model, mfg_year):
        self.car_brand = brand
        self.car_model = model
        self.car_mfg_year = mfg_year
        self.car_mileage = 0
        self.car_fuel_level = 100.0

    def drive(self, distance):
        if distance < 0:
            print("Distance cannot be negative.")
            return

        fuel_needed = distance * 0.1
        if self.car_fuel_level >= fuel_needed:
            self.car_mileage += distance
            self.car_fuel_level -= fuel_needed
            print(f"{self.car_brand} {self.car_model} drove {distance} km. New mileage: {self.car_mileage} km. Fuel level: {self.car_fuel_level}%.")
        else:
            # Drive as much as possible with the available fuel
            max_distance = self.car_fuel_level / 0.1
            self.car_mileage += max_distance
            self.car_fuel_level = 0
            print(f"{self.car_brand} {self.car_model} drove {max_distance} km before running out of fuel. New mileage: {self.car_mileage} km. Fuel level: {self.car_fuel_level}%.")

    def refuel(self, amount):
        if amount < 0:
            print("Refuel amount cannot be negative.")
            return

        if self.car_fuel_level + amount <= 100:
            self.car_fuel_level += amount
            print(f"Refueled {amount}%. New fuel level: {self.car_fuel_level}%.")
        else:
            self.car_fuel_level = 100
            print("Fuel tank is now full at 100%.")


class Fleet:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)
        print(f"Added {car.car_brand} {car.car_model} to the fleet.")

    def remove_car(self, car):
        if not self.cars:
            print("No cars in the fleet to remove.")
        else:
            try:
                self.cars.remove(car)
                print(f"Removed {car.car_brand} {car.car_model} from the fleet.")
            except ValueError:
                print(f"{car.car_brand} {car.car_model} not found in the fleet.")

    def total_mileage(self):
        total = sum(car.car_mileage for car in self.cars)
        print(f"Total mileage of the fleet: {total} km.")
        return total


# Create car objects
car1 = Car("Skoda", "Octavia", 2015)
car2 = Car("Kia", "Sportage", 2018)
car3 = Car("Volkswagen", "Passat", 2020)

# Create fleet
fleet = Fleet()

# Add cars to the fleet
fleet.add_car(car1)
fleet.add_car(car2)
fleet.add_car(car3)

# Perform some operations
car1.drive(200)
car2.drive(80)
car3.refuel(70)

# Display fleet data
fleet.total_mileage()

# Display individual car conditions
for car in fleet.cars:
    print(f"{car.car_brand} {car.car_model} - Mileage: {car.car_mileage} km, Fuel level: {car.car_fuel_level}%.")
