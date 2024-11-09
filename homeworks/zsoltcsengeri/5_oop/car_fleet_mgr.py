""" 
*Task 1: Create a file named car_fleet_mgr.py and code the solution to the following task.
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
        """
        Constructor to initialize the Car's attributes.
        :param brand: The brand of the car (e.g., "Jaguar")
        :param model: The model of the car (e.g., "E Pace")
        :param year: The year the car was manufactured
        :param mileage: Initial odometer reading, defaults to 0
        :param fuel_level: Initial fuel level, defaults to 100%
        """
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage
        self.fuel_level = fuel_level

    def get_info(self):
        """
        Display car details such as brand, model, year, mileage, and current fuel level.
        """
        print(
            f"Car info:\n brand: {self.brand}, model: {self.model}, year: {self.year}, mileage: {self.mileage}, fuel_level: {self.fuel_level}"
        )

    def drive(self, miles):
        """
        Simulate driving the car a certain distance.
        :param miles: Number of miles to drive.
        - Calculates the fuel required for the drive.
        - Checks if there is enough fuel to drive the specified distance.
        - If enough fuel, it updates the mileage and reduces the fuel level.
        - If insufficient fuel, it drives as far as possible and sets fuel to 0.
        """
        if miles < 0:
            raise ValueError(
                "Distance to drive cannot be negative"
            )  # Raise ValueError in case of a negative number

        fuel_used = miles * 0.1  # Calculate fuel required for the requested miles

        # Check if there's enough fuel to cover the distance
        if self.fuel_level >= fuel_used:
            # If enough fuel, drive the full distance
            self.mileage += miles
            self.fuel_level -= fuel_used
            print(
                f"{self.brand} {self.model} drove {miles} miles and used {fuel_used:.2f}l of fuel, fuel level: {self.fuel_level:.2f}%"
            )
        else:
            # Not enough fuel fuel, calculate possible distance and update
            max_distance = self.fuel_level / 0.1  # Max distance with remaining fuel
            self.mileage += max_distance
            self.fuel_level = 0  # Fuel is completely used up
            print(
                f"Not enough fuel for the full trip. {self.brand} {self.model} drove {max_distance:.2f} miles and ran out of fuel."
            )

    # Refuel method to fill up the tank with a given amount of fuel

    def refuel(self, amount):
        """
        Refuel the car by a specified amount.
        :param amount: Amount of fuel to add.
        - If adding the fuel exceeds 100%, sets fuel level to 100% and notifies user of excess.
        - Otherwise, adds the specified amount to the fuel level.
        """
        if amount < 0:
            raise ValueError(
                "Amount of fuel cannot be negative"
            )  # Raise ValueError in case of a negative number

        if self.fuel_level + amount > 100:
            excess = self.fuel_level + amount - 100
            self.fuel_level = 100  # Set fuel level to full
            print(
                f"The tank of {self.brand} {self.model} is now full! Could not add {excess}% as it exceeds the tank's capacity."
            )
        else:
            self.fuel_level += amount
            print(
                f"The fuel level of {self.brand} {self.model} is now at {self.fuel_level}%."
            )

    def __str__(self):
        return f"{self.brand} {self.model} {self.year} {self.mileage} {self.fuel_level}"


# Example usage:

car1 = Car(brand="Jaguar", model="E Pace", year=2018)
print(car1)
# Display initial car info
car1.get_info()

# Drive a certain distance
# This will raise a ValueError, which we catch and handle here
try:
    car1.drive(-20)
except ValueError as e:
    # Print the error message to inform the user of invalid input
    print(e)

# Attempt to refuel the car
# This will raise a ValueError, which we catch and handle here
try:
    car1.refuel(-5)
except ValueError as e:
    # Print the error message to inform the user of invalid input
    print(e)

"""
*Create a Fleet class to manage Car objects:

The class should have a list that contains the cars.
Include methods to add and remove Car objects to/from the fleet.
Include a method that aggregates the total mileage of all cars in the fleet.
Create a few Car objects, add them to the fleet, perform some operations (driving, refueling), 
and display the state of the cars and the summary data of the fleet.
"""


class Fleet:

    def __init__(self, name: str):
        self.name = name
        self.cars = []

    def add_car(self, car: Car) -> bool:
        self.cars.append(car)  # Add a car to the fleet
        return True

    def list_cars(self) -> None:
        print(f"Available cars in {self.name}: ")
        for car in self.cars:
            print(car)

    def remove_car(self, car: Car):
        if car in self.cars:
            self.cars.remove(car)
        print(f"{car} removed from the fleet.")

    def cumulative_miles(self) -> int:
        total_milage = 0
        for car in self.cars:
            total_milage += car.mileage
        return total_milage

    def __str__(self):
        return f"{self.cars}"


# Example usage:
car2 = Car("Aston Martin", "Vanquish", 2024)
car3 = Car("Lotus", "Eletre", 2024)

fleet1 = Fleet("British Car Fleet")

# Adding cars and getting immediate feedback
fleet1.add_car(car1)
fleet1.add_car(car2)
fleet1.add_car(car3)

# Performing driving operations
car1.drive(550)
car2.drive(60)
car3.drive(70)

# Removing a car and getting immediate feedback
fleet1.remove_car(car3)

# List all cars in the fleet
fleet1.list_cars()


fleet1.cumulative_miles()

# Print the total mileage of all cars in the fleet
print("Total mileage of all cars in the fleet:", fleet1.cumulative_miles())
