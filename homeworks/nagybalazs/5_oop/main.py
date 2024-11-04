"""
Készíts egy Fleet osztályt, amely kezeli a Car objektumokat:
    -   Az osztály rendelkezzen egy listával, amelyben az autók találhatóak.
    -   Tartalmazzon metódusokat Car objektumok hozzáadására és eltávolítására a flottába/flottából.
    -   Tartalmazzon egy metódust, amely összesíti a flotta összes autójának összes kilométerét. 
    -   Hozz létre néhány Car objektumot, add hozzá őket a flottához, hajts végre néhány műveletet (vezetés, tankolás), 
        jelenítsd meg az autók állapotát és a flotta összesítő adatait.
"""
from car_fleet_mgr import Car

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
    
car1 = Car("Dacia", "Duster", 2022)
car2 = Car("Ford", "Transit Connect", 2021)
car3 = Car("Ford", "Transit", 2020)


fleet = Fleet()
fleet.add_car(car1)
fleet.add_car(car2)
fleet.add_car(car3)

car1.drive(100)
car2.drive(300)
car3.drive(500)

car1.refuel(30)
car2.refuel(50)
car2.refuel(80)


total_milage = fleet.total_mileage()


fleet_summary = [(car.brand, car.model, car.mileage, car.fuel_level) for car in fleet.cars]