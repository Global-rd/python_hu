class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0
        self.fuel_level = 100

    def drive(self, distance):
        max_distance = self.fuel_level * 10
        act_distance = min(distance, max_distance)

        if max_distance < distance:
            print(f"A tüzelőanyag kifogyott, kérem töltse fel a(z) {self.brand} {self.model} autót!")

        self.mileage += act_distance
        self.fuel_level -= act_distance / 10

    def refuel(self, add):
        if self.fuel_level + add > 100:
            print(f"A tüzelőanyagot túltöltötték, a(z) {self.brand} {self.model} autónál! Takarítsa fel!")
        self.fuel_level = min(self.fuel_level + add, 100)

class Fleet:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)
        print(f"A {car.brand} {car.model} hozzáadása megtörtént")

    def remove_car(self, car):
        self.cars.remove(car)
        print(f"A {car.brand} {car.model} eltávolítása megtörtént")
        print(f"Frissített lista:")
        fleet.list_cars()

    def total_mileage(self):
        return sum(car.mileage for car in self.cars)
    
    def list_cars(self):
        for i, car in enumerate(self.cars, start=1):
            print(f"Auto {i}: {car.brand} {car.model}, megtett táv: {car.mileage} km, tüzelőanyag szint: {car.fuel_level}%")
    
if __name__ == "__main__":

    car1 = Car("Citroën", "CX", 1974)
    car2 = Car("Aston Martin", "Vantage", 1987)
    car3 = Car("Audi", "Quattro S1", 1986)
    car4 = Car("DeLorean", "DMC-12", 2085)

    fleet = Fleet()
    fleet.add_car(car1)
    fleet.add_car(car2)
    fleet.add_car(car3)
    fleet.add_car(car4)

    car1.drive(200)
    car2.drive(350)
    car1.refuel(10)
    car3.refuel(10)
    car4.drive(1200)

    fleet.list_cars()
    print(f"A flotta által összesen megtett táv: {fleet.total_mileage()} km")

    fleet.remove_car(car1)
    print(f"A flotta által összesen megtett táv: {fleet.total_mileage()} km")
