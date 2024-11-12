import logging
from datetime import datetime
import time

log_filename = "homeworks/boroczpeter/5_oop/cars.log"
filename = "homeworks/boroczpeter/5_oop/cars.txt"

logger = logging.getLogger()
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler(log_filename)
file_handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %I:%M:%S')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

class Car:
    def __init__(self, brand, model, year):
        if not isinstance(year, int) or year < 1886 or year > datetime.now().year:
            raise ValueError("The year must be an integer between 1886 and the current year.")
        
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0
        self.fuel_level = 100

    def drive(self, kilometers):
        if not isinstance(kilometers, (int, float)) or kilometers < 0:
            raise ValueError("Kilometers must be a positive number.")
        
        max_drivable_km = self.fuel_level * 10
        actual_km = min(kilometers, max_drivable_km)
        
        self.mileage += actual_km
        self.fuel_level -= actual_km * 0.1
        return actual_km

    def refuel(self, amount):
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Fuel amount must be a positive number.")
        
        self.fuel_level = min(100, self.fuel_level + amount)
    
    def __str__(self):
        return f"{self.brand} {self.model} ({self.year}) - Mileage: {self.mileage} km, Fuel Level: {self.fuel_level:.1f}%"

class Fleet:
    def __init__(self):
        self.cars = []
        self.log_action("Fleet created")

    def add_car(self, car):
        self.cars.append(car)
        self.log_action("Added car", car)

    def remove_car(self, index):
        if not isinstance(index, int) or index < 1 or index > len(self.cars):
            raise ValueError("Invalid car number.")
        
        car = self.cars.pop(index - 1)
        self.log_action("Removed car", car)
        return car

    def total_mileage(self):
        return sum(car.mileage for car in self.cars)
    
    def log_action(self, action, car=None):
        with open("homeworks/boroczpeter/5_oop/cars.txt", "a") as file:
            file.write(f"{action}, {datetime.now()}, {car if car else ''}\n")
        logger.info(f"{action} - {car if car else ''}")
    
    def list_cars(self):
        if not self.cars:
                print("There is no car in the fleet.")
        for i, car in enumerate(self.cars, 1):
            print(f"{i}. {car}")

def main():
    fleet = Fleet()

    # Create initial cars and add them to the fleet
    car1 = Car("Toyota", "Celica", 1985)
    car2 = Car("Volkswagen", "Golf", 1992)
    fleet.add_car(car1)
    fleet.add_car(car2)

    while True:
        print("\nMenu:")
        print("1. Add car to fleet")
        print("2. Remove car from fleet")
        print("3. Drive in kilometers")
        print("4. Refuel in percentage")
        print("5. List fleet cars")
        print("6. Summarize driven kilometers")
        print("7. Exit")
        
        choice = input("Choose an option: ")

        try:
            if choice == "1":
                brand = input("Enter brand: ")
                model = input("Enter model: ")
                year = int(input("Enter year: "))
                car = Car(brand, model, year)
                fleet.add_car(car)
                print(f"{car.brand} {car.model} ({car.year}) added to the list.")
                time.sleep(1)
            
            elif choice == "2":
                if not fleet.cars:
                    print("There is no car to remove.")
                    time.sleep(1)
                    continue
                fleet.list_cars()
                car_num = int(input("Enter car number to remove: "))
                if car_num < 1 or car_num > len(fleet.cars):
                    print("Invalid car number. Please select a valid car from the list.")
                    time.sleep(1)
                    continue             
                removed_car = fleet.remove_car(car_num)
                print(f"{removed_car.brand} {removed_car.model} ({removed_car.year}) removed from the list.")
                time.sleep(1)
            
            elif choice == "3":
                if not fleet.cars:
                    print("There is no car to drive")
                    time.sleep(1)
                    continue
                fleet.list_cars()
                car_num = int(input("Enter car number to drive: "))
                if car_num < 1 or car_num > len(fleet.cars):
                    print("Invalid car number. Please select a valid car from the list.")
                    time.sleep(1)
                    continue                
                kilometers = float(input("Enter kilometers to drive: "))
                car = fleet.cars[car_num - 1]
                driven_km = car.drive(kilometers)
                fleet.log_action("Drive", car)
                print(f"{car.brand} {car.model} ({car.year}) driven {driven_km} km.")
                time.sleep(1)
            
            elif choice == "4":
                if not fleet.cars:
                    print("There is no car to refuel.")
                    time.sleep(1)
                    continue
                fleet.list_cars()
                car_num = int(input("Enter car number to refuel: "))
                if car_num < 1 or car_num > len(fleet.cars):
                    print("Invalid car number. Please select a valid car from the list.")
                    time.sleep(1)
                    continue                
                fuel_amount = float(input("Enter refuel amount (percentage): "))
                car = fleet.cars[car_num - 1]
                car.refuel(fuel_amount)
                fleet.log_action("Refuel", car)
                print(f"{car.brand} {car.model} ({car.year}) has been refueled.")
                time.sleep(1)
            
            elif choice == "5":
                fleet.list_cars()
                time.sleep(1)
            
            elif choice == "6":
                total_km = fleet.total_mileage()
                print(f"Total mileage of all cars: {total_km} km")
                time.sleep(1)
            
            elif choice == "7":
                print("Exiting program.")
                break
            
            else:
                print("Invalid option. Please choose again.")
        
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()