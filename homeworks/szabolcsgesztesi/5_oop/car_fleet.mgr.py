class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0  #Kezdeti kilométeróra állás
        self.fuel_level = 100  # Kezdeti üzemanyag-szint (százalék)

    def drive(self, kilometers):
        fuel_needed = kilometers * 0.1 #Üzemanyag szükséglet kiszámítása, miszerint minden megtett kilóméter 0.1% üzemanyagot fogyaszt
        if fuel_needed > self.fuel_level: #Ellenőrizzük, hogy elengendő üzemanyag áll-e rendelkezésre
            kilometers = self.fuel_level / 0.1  #Ha nem, akkor csak annyit tudunk vezetni, amennyi üzemanyagra elegendő
            self.fuel_level = 0  #Majd ezzel az összes üzemanyag elfogy
            print(f"{self.brand} {self.model} can't drive the full distance. Only drove {kilometers} km.")
        else:
            self.fuel_level -= fuel_needed #Ha elegendő akkor megteszi az adott kilómétert
            self.mileage += kilometers
            print(f"{self.brand} {self.model} drove {kilometers} km. Fuel level is now {self.fuel_level}%.")

    def refuel(self, amount):
        if amount < 0:
            print("Can't refuel with a negative amount.")
            return
        if self.fuel_level + amount > 100:
            self.fuel_level = 100  #Maximális üzemanyag szint limit
        else:
            self.fuel_level += amount
        print(f"{self.brand} {self.model} refueled. Fuel level is now {self.fuel_level}%.")


class Fleet:
    def __init__(self):
        self.cars = []  #Lista az autók tárolására

    def add_car(self, car):
        self.cars.append(car)
        print(f"Added {car.brand} {car.model} to the fleet.")

    def remove_car(self, car):
        if car in self.cars:
            self.cars.remove(car)
            print(f"Removed {car.brand} {car.model} from the fleet.")
        else:
            print("Car not found in the fleet.")

    def total_mileage(self):
        total = sum(car.mileage for car in self.cars)
        print(f"Total mileage of the fleet: {total} km")
        return total


#Példányok létrehozása
car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Ford", "Focus", 2019)

#Flotta létrehozása és autók hozzáadása
fleet = Fleet()
fleet.add_car(car1)
fleet.add_car(car2)

#Autók vezetése
car1.drive(50)
car2.drive(300)

#Autók tankolása
car1.refuel(30)
car2.refuel(10)

#Összes kilométer összesítése
fleet.total_mileage()

#Az autók állapotának megjelenítése
for car in fleet.cars:
    print(f"{car.brand} {car.model} - Mileage: {car.mileage} km, Fuel level: {car.fuel_level}%")