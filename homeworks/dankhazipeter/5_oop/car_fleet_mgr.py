"""Flotta kezelő alkalmazás"""


class Car:
    """
    Egy autót reprezentáló osztály alapvető funkciókkal,
    ami kezeli az autó tulajdonságait (márka, modell, év, km, üzemanyag)
    és műveleteket (vezetés, tankolás).
    """

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0
        self.fuel_level = 100

    def drive(self, distance):
        """
        Szimulálja az autó haladását a megadott távolságon,
        ahol minden kilométer 0.1 egység üzemanyagot fogyaszt.
        """
        fuel_needed = distance * 0.1
        if fuel_needed <= self.fuel_level:
            self.mileage += distance
            self.fuel_level -= fuel_needed
        else:
            max_distance = self.fuel_level / 0.1
            self.mileage += max_distance
            self.fuel_level = 0
            print(f"Nincs elég üzemanyag a(z) {distance} km megtételéhez. "
                  f"Helyette {max_distance} km-t tett meg.")

    def refuel(self, amount):
        """Növeli az üzemanyagszintet a megadott mennyiséggel, de legfeljebb 100-ig."""
        if amount < 0:
            raise ValueError("A tankolás mennyisége nem lehet negatív.")
        if self.fuel_level + amount > 100:
            self.fuel_level = 100
        else:
            self.fuel_level += amount

    def __str__(self):
        return (f"{self.brand} {self.model} ({self.year}) - "
                f"Összes megtett távolság: {self.mileage} km, Üzemanyagszint: {self.fuel_level}%")


class Fleet:
    """A járműflotta kezelő osztály."""

    def __init__(self):
        self.cars = []

    def add_car(self, car):
        """Hozzáad egy autót a flottához."""

        self.cars.append(car)

    def remove_car(self, car):
        """Eltávolít egy autót a flottából."""
        if car not in self.cars:
            return
        self.cars.remove(car)

    def total_mileage(self):
        """Visszaadja a flotta összesített futásteljesítményét."""

        return sum(car.mileage for car in self.cars)

    def __str__(self):
        return f"Flotta összesített futásteljesítménye: {self.total_mileage()} km"


# Példányosítás és műveletek
car1 = Car("Audi", "Q8", 2020)
car2 = Car("BYD", "Seal", 2024)
car3 = Car("Reanult", "Zoe", 2015)

fleet = Fleet()
fleet.add_car(car1)
fleet.add_car(car2)
fleet.add_car(car3)

car1.drive(400)
car2.drive(150)
car3.drive(50)
car2.drive(500)
car1.refuel(10)
# Túl sokat tankolunk, de nem lehet több mint 100%
car1.refuel(40)
# Túl kevés üzemanyag, csak 950 km-t tud menni, ennyit megy és kiürül
car3.drive(5000)

print(car1)
print(car2)
print(car3)
print(fleet)
