from car import Car
from fleet import Fleet

car1 = Car("Dacia", "Duster", 2022)
car2 = Car("Ford", "Transit Connect", 2021)
car3 = Car("Ford", "Transit", 2020)

fleet = Fleet()
fleet.add_car(car1)
fleet.add_car(car2)
fleet.add_car(car3)

car1.drive(250)
car2.drive(350)
car3.drive(550)

car1.refuel(20)
car2.refuel(30)
car3.refuel(50)
car1.refuel(-10)

total_milage = fleet.total_mileage()

fleet.remove_car(car3)

total_milage = fleet.total_mileage()

fleet_summary = [(car.brand, car.model, car.mileage, car.fuel_level) for car in fleet.cars]