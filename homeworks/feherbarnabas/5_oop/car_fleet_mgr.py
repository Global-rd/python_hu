class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0
        self.fuel_level = 100  

    def drive(self, distance):
        fuel_needed = distance * 0.1  
        if fuel_needed <= self.fuel_level:
            self.mileage += distance
            self.fuel_level -= fuel_needed
            print(f"{self.brand} {self.model} has gone {distance} km.")
        else:
            max_distance = self.fuel_level / 0.1
            self.mileage += max_distance
            self.fuel_level = 0
            print(f"{self.brand} {self.model} went only {max_distance:.1f} km with the fuel remained.")

    def refuel(self, amount):
        if amount + self.fuel_level > 100:
            amount = 100 - self.fuel_level
        self.fuel_level += amount
        print(f"{self.brand} {self.model} got {amount}% of fuel, now it's {self.fuel_level}%.")

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year}) - Km: {self.mileage}, Fuel: {self.fuel_level}%"


class Fleet:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)
        print(f"{car.brand} {car.model} succesfully added to the fleet.")

    def remove_car(self, car):
        if car in self.cars:
            self.cars.remove(car)
            print(f"{car.brand} {car.model} removed form the fleet.")

    def total_mileage(self):
        total_km = sum(car.mileage for car in self.cars)
        print(f"Fleet's total mileage: {total_km} km")
        return total_km

    def show_fleet(self):
        for car in self.cars:
            print(car)


# Tesztelés
if __name__ == "__main__":

    car1 = Car("Lynk&Co", "01", 2020)
    car2 = Car("Polestar", "2", 2018)
    car3 = Car("Maserati", "Ghibli", 2021)

    fleet = Fleet()
    fleet.add_car(car1)
    fleet.add_car(car2)
    fleet.add_car(car3)

    car1.drive(200)
    car2.drive(150)
    car3.drive(50)

    car1.refuel(10)
    car2.refuel(20)

    fleet.total_mileage()
    fleet.show_fleet()

