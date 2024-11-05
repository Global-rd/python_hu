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
            print(f"{self.brand} {self.model} driven {distance} km. Current mileage: {self.mileage} km, Fuel level: {self.fuel_level}%")
        else:
            max_distance = self.fuel_level / 0.1
            self.mileage += max_distance
            self.fuel_level = 0
            print(f"{self.brand} {self.model} driven {max_distance} km (fuel exhausted). Current mileage: {self.mileage} km, Fuel level: {self.fuel_level}%")

    def refuel(self, amount):
        if amount < 0:
            print ("The given quantity is not correct")
            return
        elif self.fuel_level + amount > 100:
            amount = 100 - self.fuel_level
        self.fuel_level += amount
        print(f"{self.brand} {self.model} refueled by {amount}%. Current fuel level: {self.fuel_level}%")
