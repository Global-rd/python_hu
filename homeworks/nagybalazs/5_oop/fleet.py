"""
Készíts egy Car osztályt, amely rendelkezik a következő tulajdonságokkal:
    -   Márka (brand)
    -   Modell (model)
    -   Gyártási év (year)
    -   Kilométeróra állása (mileage), induló értéke 0.
    -   Üzemanyag-szint (fuel_level), induló értéke 100 (százalékban).

Az osztály tartalmazza a következő metódusokat:
    -   Egy konstruktor, amely beállítja a fenti attribútumokat.
    -   Egy drive() metódus, amely adott számú kilométerrel növeli a kilométeróra állását, 
        és csökkenti az üzemanyag-szintet (tételezzük fel, hogy 0.1% üzemanyag fogy megtett kilométerenként). 
        A drive() metódus csak annyit km-et engedjen vezetni, amennyire elegendő üzemanyag van.
    -   Egy refuel() metódus, amely feltölti az üzemanyag-szintet egy adott mennyiséggel. Figyelj a limitekre.
"""

class Fleet:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)
        print(f"{car.brand} {car.model} added to fleet.")

    def remove_car(self, car):
        if car in self.cars:
            self.cars.remove(car)
            print(f"{car.brand} {car.model} removed from fleet.")
        else:
            print(f"{car.brand} {car.model} not found in fleet.")

    def total_mileage(self):
        total = sum(car.mileage for car in self.cars)
        print(f"Total fleet mileage: {total} km")
        return total