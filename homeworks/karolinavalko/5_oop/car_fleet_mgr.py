from modules import Car
from modules import Fleet

car_1 = Car("Toyota", "CHR", 2018)
car_2 = Car("Tesla", "S-type", 2023)
car_3 = Car("Ford", "Mustang GT", 1968)

fleet_1 = Fleet("Test_fleet")
fleet_1.add_car_to_fleet(car_1)
fleet_1.add_car_to_fleet(car_2)
fleet_1.add_car_to_fleet(car_3)
fleet_1.list_of_cars()
fleet_1.cars[0].drive(30)
fleet_1.cars[1].drive(50)
fleet_1.cars[2].drive(150)
car_1.refuel(20)
fleet_1.remove_car_from_fleet(2)
fleet_1.total_fleet_mileage()
