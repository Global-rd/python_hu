class Car:
    def __init__(self, brand, model, year):
        
#Konstruktor, amely beállítja a Márka, Modell, Gyártási év attribútumokat.
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0  # Kilométeróra állás kezdőértéke
        self.fuel_level = 100  # Üzemanyagszint kezdőértéke (százalékban)
    
    
    def drive(self, distance):
#A megadott távolságot megpróbálja megtenni, csökkenti az üzemanyagszintet, és növeli a kilométeróra állását.
        max_distance = self.fuel_level / 0.1  # Ennyit tud megtenni a jelenlegi üzemanyagszinttel
        actual_distance = min(distance, max_distance)
        
# Km növelése és üzemanyag csökkentése
        self.mileage += actual_distance
        self.fuel_level -= actual_distance * 0.1
        print(f"{self.brand} {self.model} drove {actual_distance} km. Current mileage: {self.mileage} km, fuel level: {self.fuel_level:.2f}%")
    

#Üzemanyag feltöltése a megadott mennyiséggel, de legfeljebb 100%-ig.    
    def refuel(self, amount):
        new_fuel_level = min(self.fuel_level + amount, 100)
        refueled_amount = new_fuel_level - self.fuel_level
        self.fuel_level = new_fuel_level
        print(f"{self.brand} {self.model} refueled by {refueled_amount}%. Current fuel level: {self.fuel_level:.2f}%")

class Fleet:
#Konstruktor, amely inicializálja az autók listáját.
    def __init__(self):
        self.cars = []
    
    
#Új autó hozzáadása a flottához.
    def add_car(self, car):
        self.cars.append(car)
        print(f"Added {car.brand} {car.model} to the fleet.")
   
    
 #Autó eltávolítása a flottából.   
    def remove_car(self, car):
        if car in self.cars:
            self.cars.remove(car)
            print(f"Removed {car.brand} {car.model} from the fleet.")
        else:
            print(f"{car.brand} {car.model} not found in the fleet.")
  
    
#A flotta összes autójának összesített kilométerórája.
    def total_mileage(self):
        total = sum(car.mileage for car in self.cars)
        print(f"Total mileage of the fleet: {total} km")
        return total


# Példa használat:
if __name__ == "__main__":
    # Autók létrehozása
    car1 = Car("Volkswagen", "Golf", 2020)
    car2 = Car("Dodge", "Challenger", 2023)
    car3 = Car("Honda", "Civic", 2021)
    
    # Flotta létrehozása és autók hozzáadása
    fleet = Fleet()
    fleet.add_car(car1)
    fleet.add_car(car2)
    fleet.add_car(car3)
    
    # Műveletek: vezetés és tankolás
    car1.drive(133)  
    car2.drive(487)  
    car1.refuel(23)  
    car3.drive(67)   
    
    # Flotta összes kilométerének kiírása
    fleet.total_mileage()
    
    # Autók állapotának megjelenítése
    print("\nFleet status:")
    for car in fleet.cars:
        print(f"{car.brand} {car.model} - Mileage: {car.mileage} km, Fuel Level: {car.fuel_level:.2f}%")
