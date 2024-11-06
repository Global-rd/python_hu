"""Hozz létre egy car_fleet_mgr.py nevű file-t, és kódold le a következő feladat megoldását:

OK  - Készíts egy Car osztályt, amely rendelkezik a következő tulajdonságokkal:
OK      ● Márka (brand)
OK      ● Modell (model)
OK      ● Gyártási év (year)
OK      ● Kilométeróra állása (mileage), induló értéke 0.
OK      ● Üzemanyag-szint (fuel_level), induló értéke 100 (százalékban).

- Az osztály tartalmazza a következő metódusokat:
OK      ● Egy konstruktor, amely beállítja a fenti attribútumokat.
OK      ● Egy drive() metódus, amely adott számú kilométerrel növeli a kilométeróra állását, és csökkenti az üzemanyag-szintet (tételezzük fel, hogy 0.1% üzemanyag fogy megtett kilométerenként). A drive() metódus csak annyit km-et engedjen vezetni, amennyire elegendő üzemanyag van.
OK      ● Egy refuel() metódus, amely feltölti az üzemanyag-szintet egy adott mennyiséggel. Figyelj a limitekre.

OK  - Készíts egy Fleet osztályt, amely kezeli a Car objektumokat:
OK      ● Az osztály rendelkezzen egy listával, amelyben az autók találhatóak.
OK      ● Tartalmazzon metódusokat Car objektumok hozzáadására és eltávolítására a flottába/flottából.
OK      ● Tartalmazzon egy metódust, amely összesíti a flotta összes autójának összes kilométerét.
OK      ● Hozz létre néhány Car objektumot, add hozzá őket a flottához, hajts végre néhány műveletet (vezetés, tankolás), jelenítsd meg az autók állapotát és a flotta összesítő adatait."""

##############################################################################
######################## I. Osztályok létrehozása:############################
##############################################################################

import os
from datetime import datetime as dt

######################## "Car" osztály létrehozása:###########################
class Car:
    # Konstruktor létrezhozása, ami beállítja a kért attribútomokat (márka, modell, év + km óra, benzin szint):
    def __init__(self, brand: str, model: str, year: int):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0                    # km
        self.fuel_level = 100               # %

    # Drive() metódus definiálása:
    def drive(self, kilometers):
        fuel_needed = kilometers * .1
        if self.fuel_level > fuel_needed:
            self.mileage += kilometers
            self.fuel_level -= fuel_needed
        else:
            print(f'Nincs elég benzin.')

    # Refuel() metódus definiálása:
    def refuel(self, liter):
        if liter > 0:
            if self.fuel_level + liter > 100:   # ezt itt úgy kezelem le, hogy ha több lenne, mint a max. 100 l, akkor csak addig lehessen tölteni
                self.fuel_level = 100
            else:
                self.fuel_level += liter
        else:
            print(f"Benzint leszívni nem ér! Adj meg pozitív értéket a megadott {liter} liter helyett.")

    # A __str__ metódus behozása, "olvashatóan" formázott string visszadásához a print-nél:
    def __str__(self):
        return(f"Autó: {self.brand} {self.model} ({self.year})  |  Megtett út: {self.mileage} km  |  Üzemanyagszint (beleszámítva a tankolást is, ha volt): {self.fuel_level} %")


######################## "Fleet" osztály létrehozása:#########################
class Fleet:
    # Konstruktor létrezhozása, a flotta autóinak listája:
    def __init__(self):
        self.cars = []
    
    # autó hozzáadása metódus definiálása:
    def add_car(self, car: Car):
        self.cars.append(car)

    # autó eltávolítása metódus definiálása:
    def remove_car(self, car: Car):
        if car in self.cars:
            self.cars.remove(car)
    # összes megtett km metódus definiálása:
    def total_mileage(self):
        return sum(car.mileage for car in self.cars)
    
    # A __str__ metódus behozása, "olvashatóan" formázott string visszadásához a print-nél:
    def __str__(self):
        return "\n".join(str(car) for car in self.cars)


##############################################################################
########################## II. Teszt környezet:###############################
##############################################################################

current_datetime = dt.now()

os.system("cls")
print(f"(Előző futási eredmény törölve a képernyőről ekkor: {current_datetime})")
print("----------------------------")

if __name__ == "__main__":
# Car objektumok definiálása, a Car osztály meghívásával):
    my_car1 = Car("Skoda", "Scala", 2022)
    my_car2 = Car("Honda", "Accord", 2018)
    my_car3 = Car("Volvo", "XC40", 2020)

#Vezetés (drive() metódus tesztelése):   
    my_car1.drive(10)
    my_car2.drive(30)
    my_car3.drive(50)

# Tankolás (refuel() metódus tesztelése):
    my_car1.refuel(-.1)
    my_car2.refuel(.1)

# Car objektumok hozzáadása, a Fleet osztály meghívásával:
    fleet = Fleet()
    fleet.add_car(my_car1)
    fleet.add_car(my_car2)
    fleet.add_car(my_car3)

# A flotta aktuális állapotának megjelenítése:
    print("Az aktuális flotta részletei:\n")
    print(fleet)
    print("----------------------------")
    print(f"A flotta által megtett összes km: {fleet.total_mileage()} km")
    print("----------------------------")

# Car objektumok eltávolítása:
    fleet.remove_car(my_car3)
    print(f"A kiválasztott autó eladása után az alábbi autók maradtak a flottában:\n\n{fleet}")