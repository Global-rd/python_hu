# Create class Car
class Car:
    #Attributes
    def __init__(self, brand: str, model: str, year: int):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0
        self.fuel_level = 100

    #Methods
    def drive(self, distance: float):
        fuel_needed = distance * 0.1
        if fuel_needed <= self.fuel_level:
            self.mileage += distance
            self.fuel_level -= fuel_needed
            print(f"Driven {distance} km. Mileage: {self.mileage} km. Fuel level: {self.fuel_level}%.")
        else:
            max_distance = self.fuel_level / 0.1
            self.mileage += max_distance
            self.fuel_level = 0
            print(f"Not enough fuel for the planned {distance} km. Max distance is {max_distance} km.")

    def refuel(self, amount: float):
        if amount < 0:
            print("Refuel amount must be a positive number")
            return     
        elif amount + self.fuel_level > 100:
            self.fuel_level = 100
        else:
            self.fuel_level += amount
        print(f"Refueled {amount}%. Fuel level: {self.fuel_level}%.")

# Create class Fleet
class Fleet:
    def __init__(self):
        self.cars = []

    def add_car(self, car: Car):
        self.cars.append(car)
        print(f"Added {car.brand} {car.model} to the fleet.")

    def remove_car(self, car: Car):
        if car in self.cars:
            self.cars.remove(car)
            print(f"Removed {car.brand} {car.model} from the fleet.")
        else:
            print(f"{car.brand} {car.model} is not in the fleet.")

    def total_mileage(self):
        total = sum(car.mileage for car in self.cars)
        print(f"Total mileage of the fleet is {total} km.")
        return total
    
if __name__ == "__main__":
    # Create cars
    car1 = Car("Toyota", "Corolla", 2020)
    car2 = Car("Ford", "Mustang", 2018)
    car3 = Car("Tesla", "Model S", 2022)

    # Create fleet
    fleet = Fleet()

    # Adding cars to the fleet
    fleet.add_car(car1)
    fleet.add_car(car2)
    fleet.add_car(car3)

    # Drive / refuel cars
    car1.drive(55)
    car2.drive(125)
    car3.refuel(25)
    car3.drive(500)

    # Total milage of the fleet
    fleet.total_mileage()