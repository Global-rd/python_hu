class Car:
    def __init__(self, brand, model, year, fuel_consumption):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0
        self.fuel_level = 100
        self.fuel_consumption = fuel_consumption  # liter/100km

    def drive(self, kilometers):
        if kilometers < 0:
            raise ValueError("A megtett távolság nem lehet negatív.")

        required_fuel = kilometers * self.fuel_consumption / 100
        if required_fuel > self.fuel_level:
            max_km = self.fuel_level / (self.fuel_consumption / 100)
            print(f"Nincs elég üzemanyag, csak {max_km:.1f} km-t tudsz megtenni.")
            self.mileage += max_km
            self.fuel_level = 0
        else:
            self.mileage += kilometers
            self.fuel_level -= required_fuel
            if self.fuel_level < 0:
                self.fuel_level = 0
                print("Az autó leállt üzemanyaghiány miatt.")

        print(f"{self.brand} {self.model} üzemanyag szint: {self.fuel_level}%, kilométeróra állása: {self.mileage} km")

    def refuel(self, amount):
        if amount < 0:
            print("A tankolási mennyiség nem lehet negatív.")
            return
        new_fuel_level = self.fuel_level + amount
        if new_fuel_level > 100:
            self.fuel_level = 100
            print("Az üzemanyag-szint elérte a maximumot (100%).")
        else:
            self.fuel_level = new_fuel_level
        print(f"{self.brand} {self.model} üzemanyag szint: {self.fuel_level}%")

class Fleet:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)
        print(f"{car.brand} {car.model} hozzáadva a flottához.")

    def remove_car(self, car):
        if car in self.cars:
            self.cars.remove(car)
            print(f"{car.brand} {car.model} eltávolítva a flottából.")
        else:
            print("Az autó nem található a flottában.")

    def total_mileage(self):
        total = sum(car.mileage for car in self.cars)
        print(f"A flotta összesített kilométere: {total} km")
        return total

    def display_fleet_status(self):
        print("Flotta állapota:")
        for car in self.cars:
            print(f"{car.brand} {car.model}, Évjárat: {car.year}, Kilométeróra: {car.mileage} km, Üzemanyag: {car.fuel_level}%")

# Példa használat
if __name__ == "__main__":
    # Létrehozunk néhány Car objektumot
    car1 = Car("Toyota", "Corolla", 2019, 6)  # 6 liter/100km
    car2 = Car("Ford", "Focus", 2020, 7)  # 7 liter/100km
    car3 = Car("Honda", "Civic", 2018, 5)  # 5 liter/100km

    # Létrehozunk egy Fleet objektumot és hozzáadjuk az autókat
    fleet = Fleet()
    fleet.add_car(car1)
    fleet.add_car(car2)
    fleet.add_car(car3)

    # Vezetés és tankolás műveletek végrehajtása
    car1.drive(150)
    car1.refuel(20)
    car2.drive(50)
    car3.drive(200)

    # Flotta állapotának megjelenítése
    fleet.display_fleet_status()

    # Flotta összesített kilométerének kiírása
    fleet.total_mileage()