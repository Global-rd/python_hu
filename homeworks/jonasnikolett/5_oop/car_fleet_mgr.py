# Készíts egy Car osztály, amely rendelkezik a következő tulajdonságokkal
class Car:          #osztály
    def __init__(self, brand: str, model: str, year: int):
        self.brand = brand  #márka
        self.model = model   #modell
        self.year = year    #gyártási év 
        self.mileage = 0    #km óra állása induló érték 0
        self.fuel_level = 100   #üzemanyagszint százalékban

    #Methods
    def drive(self, distance: float):
        fuel_needed = distance * 0.1        #km-növeéi és az üzemanyagot csökkenti a fogyasztás függvényében
        if fuel_needed <= self.fuel_level:
            self.mileage += distance
            self.fuel_level -= fuel_needed
            print(f"Vezetni lehet {distance} km. Kilóméter óra induló állása: {self.mileage} km.")
        elif distance <=0:
            print(f"A megadatott táv negatív, ami nem lehetséges ({distance} km.)")
        else:
            max_distance = self.fuel_level / 0.1
            self.mileage += max_distance
            self.fuel_level = 0
            print(f"Nincs elég üzemanyag a tervezett {distance} km-es távoltságra. Maximum {max_distance} km tehető meg.")

    def refuel(self, amount: float):        #üzemanyag feltöltés
        if amount < 1:
            print("Refuel/tankolás értékének nagyobnak kell lenni-e mint 1")
            return     
        elif amount + self.fuel_level > 99:
            self.fuel_level = 100
        else:
            self.fuel_level += amount
        print(f"Feltöltve {amount}%. Aktuális töltöttségi állapot {self.fuel_level}%.")


class Fleet:            #Fleet osztály létrehozása amely kezeli a Car objektmokat
    def __init__(self):
        self.cars = []

    def add_car(self, car: Car):
        self.cars.append(car)
        print(f"A {car.brand} {car.model} hozzálett adva a flottához.")

    def remove_car(self, car: Car):
        if car in self.cars:
            self.cars.remove(car)
            print(f"A {car.brand} {car.model} törölve lett a flottából.")
        else:
            print(f"A {car.brand} {car.model} nem található a flottában")

    def total_mileage(self):
        total = sum(car.mileage for car in self.cars)
        print(f"A foltta összez gépjárműjének megtett összes kilómétere {total} km.")
        return total
    
if __name__ == "__main__":
    car1 = Car("Audi", "A4", 2023)
    car2 = Car("BMW", "X5", 2018)
    car3 = Car("Skoda", "Fábia", 2020)
    car4 = Car("Wolksvagen", "Passat", 2024)
    fleet = Fleet()
    fleet.add_car(car1)
    fleet.add_car(car2)
    fleet.add_car(car3)
    fleet.add_car(car4)




    fleet.total_mileage()  #összes km