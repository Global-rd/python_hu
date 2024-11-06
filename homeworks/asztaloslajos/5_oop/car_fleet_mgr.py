"""
to_do.py --- Asztalos Lajos --- 2024.11.01
"""
# Car
class Car:
    car_id = 0
    def __init__(self, brand, model, year:int):
        Car.car_id += 1
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0
        self.fuel_level = float(100)
        self._id = Car.car_id

# Car str method update
    def __str__(self):
        return f"Azonosító: {self._id}, Gyártó: {self.brand}, Modell: {self.model}, Gyártási év: {self.year}, Futott kilométer:{self.mileage} Üzemanyagszint: {self.fuel_level}%"

# Car drive method
    def drive(self, distance:int) -> bool:
        fuel_consumption = distance * 0.1
        if distance <= 0:
            print("Nem megfelelő kilométerértéket adtál meg!\n")
            return False
        elif self.fuel_level-fuel_consumption >= 0:
            self.fuel_level -= fuel_consumption
            self.mileage += distance
            return True
        else:
            print("Túl sok megtett kilométert adtál meg!\n")
            return False

# Car refuel method
    def refuel(self,fuel:float) -> bool:
        if fuel <=0:
            print("Nem megfelelő üzemanyagtöltési értéket adtál meg!\n")
            return False
        elif self.fuel_level + fuel <=100:
            self.fuel_level += fuel
            return True
        else:
            print("Túl sok üzemanyagmennyiséget adtál meg!\n")
            return False
# Fleet
class Fleet:

    def __init__(self):
        self.cars = []

# Fleet list_car method  
    def list_car(self) -> None:
        print("Az autók listája:")
        for car in self.cars:
            print(car)

# Fleet add_car method
    def add_car(self, car: Car) -> bool:
        self.cars.append(car)
        return True

# Fleet remove_car method   
    def remove_car(self, car:Car) -> bool:
        if car in self.cars:
            self.cars.remove(car)
            print("Sikeresen eltávolítva a flottából.\n")
            return True
        print("Nincs ilyen autó!\n")
        return False

# Fleet sum_cars_mileage method    
    def sum_cars_mileage(self):
        sum_mileage = 0
        for car in self.cars:
            sum_mileage += car.mileage
        return sum_mileage

# test data
fleet = Fleet()
fleet.add_car(Car(brand="Toyota", model="Corolla", year=1998))
fleet.add_car(Car(brand="Lancia", model="Delta", year=2013))
fleet.add_car(Car(brand="Fiat", model="Panda", year=2017))
# list all cars data
print(fleet.list_car())
# print sum millage of cars
print(f"Összes megtett út: {fleet.sum_cars_mileage()} km\n")

# test oparations
fleet.cars[1].drive(distance=-5) # wrong value
fleet.cars[1].drive(distance=1000)
fleet.cars[1].drive(distance=500) # wrong value
fleet.cars[2].drive(distance=1000)
fleet.cars[2].refuel(fuel=-20) # wrong value
fleet.cars[2].refuel(fuel=120) # wrong value
fleet.cars[2].refuel(fuel=20)
fleet.remove_car(Car("Suzuki","Ignis",2001)) # wrong value
fleet.remove_car(fleet.cars[1])
fleet.add_car(Car(brand="Skoda", model="Octavia", year=1999))
fleet.add_car(Car(brand="Fiat", model="Tipo", year=2001))

# list all cars data
print(fleet.list_car())
# print sum millage of cars
print(f"Összes megtett út: {fleet.sum_cars_mileage()} km")
