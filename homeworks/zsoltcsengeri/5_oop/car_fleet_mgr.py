""" 
*Task 1: todo Create a file named car_fleet_mgr.py and code the solution to the following task.
!Create a Car class that has the following attributes: 
Brand (brand) Model (model) Year of manufacture (year) odometer reading (mileage), starting value is 0. 
Fuel level (fuel_level), starting value is 100 (in percentage). 
The class should include the following methods: 
A constructor that initializes the above attributes. 
A drive() method, which increases the odometer reading by a given number of miles.
and decreases the fuel level (assume 0.1% fuel consumption per kilometer driven). 
The drive() method should only allow driving as many miles as there is sufficient fuel for. 
A refuel() method, which refills the fuel level by a specified amount. Be mindful of the limits. 
"""


class Car:

    def __init__(self, brand, model, year, mileage=0, fuel_level=100):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage
        self.fuel_level = fuel_level

    def get_info(self):
        print(
            f"Car info:\n brand: {self.brand}, model: {self.model}, year: {self.year}, mileage: {self.mileage}, fuel_level: {self.fuel_level}"
        )

    def drive(self, miles):
        # Calculate fuel required for the requested miles
        fuel_used = miles * 0.1

        # Check if there's enough fuel to cover the distance
        if self.fuel_level >= fuel_used:
            # Sufficient fuel, proceed with the drive
            self.mileage += miles
            self.fuel_level -= fuel_used
            print(
                f"{self.brand} {self.model} drove {miles} miles and used {fuel_used:.2f}l of fuel, fuel level: {self.fuel_level:.2f}%"
            )
        else:
            # Insufficient fuel, calculate possible distance and update
            max_distance = self.fuel_level / 0.1
            self.mileage += max_distance
            self.fuel_level = 0  # Fuel is completely used up
            print(
                f"Not enough fuel for the full trip. {self.brand} {self.model} drove {max_distance:.2f} miles and ran out of fuel."
            )

    # Refuel method to fill up the tank with a given amount of fuel

    def refuel(self, amount):

        if self.fuel_level + amount > 100:
            self.fuel_level = 100

            print(f"The tank of {self.brand} {self.model} is full!")

        else:
            self.fuel_level += amount
            print(f"The fuel level of {self.brand} {self.model} {self.fuel_level}  ")


car1 = Car(brand="Jaguar", model="E Pace", year=2018)

# Call the drive method by passing a number as a distance
car1.drive(100)
# Call the refuel method by passing a number as the amount of refill
car1.refuel(5)
