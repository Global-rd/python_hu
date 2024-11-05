
class Car:

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0 # Starting km
        self.fuel_level = 100 # Starting fuel level %

    def drive(self,kilometer):
        try:
            if kilometer < 0:
                raise ValueError ("You can't move negative distance")
            
            max_driveable_kilometer = self.fuel_level /0.1
            if kilometer > max_driveable_kilometer:
                print(f"Not enough fuel! You can drive only {max_driveable_kilometer:.1f} km")
                kilometer = max_driveable_kilometer
            
            if kilometer > 0:
                self.mileage += kilometer
                self.fuel_level -= kilometer * 0.1

        except ValueError as e:
            print("Error happened: {e}")


    def refuel(self, amount):
        try:
            if amount < 0:
                 raise ValueError("Fuel level can't be negative")

            new_fuel_level = self.fuel_level + amount

            if new_fuel_level > 100:
                print("Fuel level can't go above 100%")
                self.fuel_level = 100
            else:
                self.fuel_level = new_fuel_level
        except ValueError as e:
            print(f"Error happened: {e}")


    def __str__(self):
        return (f"{self.brand} {self.model} ({self.year}): "
                f"{self.mileage} km, Fuel: {self.fuel_level:.1f}%")
    

class Fleet:
    def __init__(self):
        self.cars = []  # cars list

    def add_car(self, car):
        if isinstance(car, Car):
            self.cars.append(car)
        else:
            print("Please add 'Brand', 'Model' and 'Year'.")

    def remove_car(self, car):
        try:
            self.cars.remove(car)
        except ValueError:
            print("This car is not on the list.")

    def total_mileage(self):
        return sum(car.mileage for car in self.cars)

    def __str__(self):
        fleet_status = "\n".join(str(car) for car in self.cars)
        return f"Fleet status:\n{fleet_status}\n Sum km: {self.total_mileage()} km"   


# Example
if __name__ == "__main__":
    # Creating cars
    car1 = Car("Volkswagen", "Golf", 2010)
    car2 = Car("Ford", "Focus", 2015)
    car3 = Car("Tesla", "Model 3", 2020)

    # Fleet creating and car addition
    fleet = Fleet()
    fleet.add_car(car1)
    fleet.add_car(car2)
    fleet.add_car(car3)

    # Methods
    car1.drive(150)  # Driving 150 km
    car2.drive(50)   # Driving 50 km-t
    car2.drive(1000)
    car3.refuel(-20)  # Wrong input test
    car3.refuel(30)  # Refueling 30%
    
    # Results
    print(fleet)  # Fleet status