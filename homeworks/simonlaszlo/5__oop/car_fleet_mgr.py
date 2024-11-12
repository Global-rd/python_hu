
class Car:
    """
    Car osztaly, a járművek tulajdonságaival.
    """
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0 
        self.fuel_level = 100 

    def drive(self, kilometers):
        """
        A megtett kilóméterekkel növeli az óra állását, csökkenti
        az üzemanyag szintet. Ellenörzi, elég-e az üzemanyag.
        """
        fuel_needed = kilometers * 0.1
        if kilometers < 0:
            print("Nem adhatsz negatív értéket!")
        elif kilometers == 0:
            print("Nem adhatsz nemeg 0-át!")   
        elif fuel_needed > self.fuel_level: 
            kilometers = round(self.fuel_level / 0.1)
            print(f"Nem eleg az uzemanyag! Csak {kilometers} km-t tudsz megtenni.")
        else:
            self.mileage += kilometers
            self.fuel_level -= fuel_needed
            print(f"{kilometers} km-t tettel meg. Jelenlegi kilometerora allas: {self.mileage} km, uzemanyag-szint: {self.fuel_level}%")

    def refuel(self, fill):
        """
        Az üzemanyagszint feltöltését kezeli, tartományt ellenőriz.
        """
        if fill < 0:
            print("Ne lopd az uzemanyagot!")
            return
        elif fill == 0:
            print("Nem tankoltal!")
            return
        elif (self.fuel_level+fill) > 100:
            print("Ennyi nem fer bele!")
            return
        else:
            self.fuel_level += fill

        print(f"{fill}% uzemanyagot tankoltal. Jelenlegi uzemanyagszint: {self.fuel_level:.1f}%")

class Fleet:
    """
     Fleet osztály, kezeli a Car objektumokat
    """
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        """
        Jármű flottába illesztése.
        """
        self.cars.append(car)
        print(f"{car.brand} {car.model} auto hozzaadva a flottahoz.")

    def remove_car(self, car):
        """
        Jármű eltávolítása
        """
        if car in self.cars:
            self.cars.remove(car)
            print(f"{car.brand} {car.model} auto eltavolitva a flottabol.")
        else:
            print(f"{car.brand} {car.model} auto nincs a flottaban!")

    def total_mileage(self):
        """
        Kiszámolja az eddig összes járművel megtett utat.
        """
        totalkm = sum(car.mileage for car in self.cars)
        print(f"A flotta osszes autojanak osszes kilometerora allasa: {totalkm} km")
        return totalkm


fleet = Fleet()

    # Autók létrehozása
car1 = Car("Toyota", "Previa", 2005)
car2 = Car("Ford", "Escort", 1998)
car3 = Car("Trabant", "601", 1976) 

    # Autók hozzáadása a flottához
fleet.add_car(car1)
fleet.add_car(car2)
fleet.add_car(car3)

    # Autók vezetése
car1.drive(50)
car2.drive(200)
car3.drive(550)

    # Üzemanyag tankolása
car1.refuel(-20)
car2.refuel(100)
car3.refuel(10)

    # Flotta összes kilométeróra állásának kiírása
fleet.total_mileage()
