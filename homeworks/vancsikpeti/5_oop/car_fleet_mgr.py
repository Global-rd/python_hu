class Car:
    total_distance = 0.0

    def __init__(self, brand: str, model: str, year: int, mileage = 0, fuel_level = 100):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage # induló értéke 0
        self.fuel_level = fuel_level # induló értéke 100, tételezzük fel, hogy 0.1% üzemanyag fogy megtett kilométerenként
   
    #def new_car(self):
        #self.brand = input("Brand of car: ")
        #self.model = input("Model of car: ")
        #self.year = input("Product year: ")
        #self.fuel_level = 100
        #self.mileage = 0

    def show_cars_condition(self):
        print(f"{self.brand}-{self.model} ({self.year}): distance->{self.mileage} miles, fuel level->{self.fuel_level}%")
    
    def __str__(self):
        return f"{self.brand}-{self.model} ({self.year})"
    
    def enter_miles(self):
        while True:
            try: 
                miles = int(input(f"How many miles did you drive with {self}? "))
            except ValueError or TypeError:
                print("Please enter a positive whole number.")
                continue
            if miles < 0:
                print("Please enter a positive whole number.")
            # fuel check
            elif miles * 0.1 > self.fuel_level:
                print(f"Not enough fuel in {self}. The fuel level is {self.fuel_level}%.")
            else: break
        return miles

    def drive(self, miles):
        self.mileage += miles
        self.fuel_level -= miles * 0.1
        print(f"{self} traveled {miles} miles.")
        Car.total_distance += miles
    
    def refuel(self):
        while True:
            try: 
                fueled_quantity = float(input(f"How many percent of fuel level do you want to refuel into {self}? "))
            except ValueError or TypeError:
                print("Please enter a positive whole number as percent. (except error)")
                continue
            if self.fuel_level + fueled_quantity > 100:
                print(f"Is to much. You should only {100-self.fuel_level} refuel to full tank. (refuel error)")
            elif fueled_quantity < 0.0:
                print("Please enter a positive whole number. (negativ error)")
            else: 
                self.fuel_level += fueled_quantity
                print(f"{self} is refuled: {self.fuel_level}")
                break
        return self.fuel_level 

class Fleet(Car):
    
    def __init__(self, name):
        self.name = name
        self.cars = []

    def new_car_to_fleet(self, brand: Car):
        self.cars.append(brand)
        print(f"New car in the fleet: {brand}")
        return True

    def remove_car_from_fleet(self, brand: Car):
        for car in self.cars:
            if car.brand == brand:
                self.cars.remove(car)
                print(f"Car remove from the fleet: {car}")
                return
        print(f"No car found with this brand: {brand}")

    def available_cars(self):
        print("Available cars: ")
        for car in self.cars:
            print(f" - {car}")


fleet_1 = Fleet(name="fleet")    

car_1 = Car(brand="Mazda", model="6", year=2018)
fleet_1.new_car_to_fleet(car_1)
car_2 = Car(brand="Renault", model="Megane", year=2017)
fleet_1.new_car_to_fleet(car_2)
fleet_1.available_cars()

car_1.drive(car_1.enter_miles())
car_1.show_cars_condition()
car_2.drive(car_2.enter_miles())
car_2.show_cars_condition()

car_3 = Car(brand="Kia", model="Ceed", year=2020)
fleet_1.new_car_to_fleet(car_3)
car_4 = Car(brand="Peugeot", model="406", year=2019)
fleet_1.new_car_to_fleet(car_4)
fleet_1.available_cars()

fleet_1.remove_car_from_fleet(car_4.brand)
fleet_1.available_cars()

car_3.drive(car_3.enter_miles())
car_3.show_cars_condition()
car_3.refuel()
car_3.show_cars_condition()

print(f"The distance traveled by the cars in the fleet: {Fleet.total_distance}")