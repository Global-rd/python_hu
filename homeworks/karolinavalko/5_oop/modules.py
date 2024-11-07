class Car:

    def __init__(self, car_brand: str, car_model: str, production_year: int):
        self.car_brand = car_brand
        self.car_model = car_model
        self.production_year = production_year
        self.car_mileage = 0
        self.car_fuel_level = 100

    def __str__(self):
        return f"{self.car_brand}, {self.car_model}, {self.production_year}"

    def drive(self, distance: float):
        if distance < 0:
            print("Please give a positive number for distance.")
            return
        fuel_spent = 0.1 * distance
        if self.car_fuel_level >= fuel_spent:
            self.car_mileage += distance
            self.car_fuel_level -= fuel_spent
            print(
                f"For car: {self}: \nDriving status: {distance} km. \nMilage status: {self.car_mileage} km. \nCurrent fuel level: {self.car_fuel_level}."
            )
        else:
            allowed_distance = self.car_fuel_level / 0.1
            print(f"You only have enough fuel for {allowed_distance} km.")

    def refuel(self, refill_percent: float):
        try:
            float(refill_percent)
        except ValueError:
            print("Please give a positive number in numeric format.")
            return
        if self.car_fuel_level + refill_percent > 100:
            print(f"You can only fill {100-self.car_fuel_level} % for {self}. ")
            return
        if refill_percent < 0 :
            print("Please give a positive number.")
            return
        self.car_fuel_level += refill_percent
        print(f"The new fuel level is {self.car_fuel_level} % for {self}.")


class Fleet:
    def __init__(self, name: str):
        self.name = name
        self.cars = []

    def add_car_to_fleet(self, car: Car) -> str:
        self.cars.append(car)
        return f"You succesfully addedd {car.car_brand}, {car.car_model} of {car.production_year}."

    def list_of_cars(self):
        for number, item in enumerate(self.cars, 1):
            print(f"{number}. {item}")

    def remove_car_from_fleet(self, car):
        if car in self.cars:
            self.cars.remove(car)
            print(f"You successfully removed {car} from the fleet.")    
        else:
            print(f"This car is not member of the fleet")
    

    def total_fleet_mileage(self) -> str:
        total_miles = 0
        for car in self.cars:
            total_miles += car.car_mileage
        print(f"Total miles in {self.name}: {total_miles} km.")
        return total_miles
