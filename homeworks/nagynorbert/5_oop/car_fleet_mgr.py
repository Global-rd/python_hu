# Homework 5. Nagy Norbert
import car_fleet_mpr_classes as car_classes
import random

file_path = "homeworks/nagynorbert/5_oop/cars.txt"

def input_cars_from_file():
    """Read input data about cars from file. Writes into a list as car objects."""
    car_object_list = []
    with open(file_path,"r") as file:
        for line in file:
            car = line.strip()
            #cars.append(car)
            car_attr = car.split(",")
            if len(car_attr) != 3:
                raise car_classes.CarDefineError("Number of parameters for define a car is not met with specification. Please check input file!")
            c_brand = car_attr[0]
            c_model = car_attr[1]
            c_year = car_attr[2]
            car_obj = car_classes.Car(c_brand,c_model,c_year)
            car_object_list.append(car_obj)            
    
    return car_object_list

def define_car_manually():
    """Define car from terminal inputs"""
    print("Please define a car:")
    brand = input("Brand: ")
    model = input("Model: ")
    try:
        year = int(input("Year: "))
    except ValueError as e:
        print(f"Year has to be integer! {e}")
    else:
        car = car_classes.Car(brand.strip(),model.strip(),year)

    print(f"User defined car: {car} ")

    return car

def add_car_to_fleet_manually(fleet:car_classes.Fleet):
    """Define car from terminal add add it into a fleet"""
    car = define_car_manually()
    print(f"{car} is added to {fleet}")
    fleet.add_car_to_fleet(car)

def remove_car_manually(fleet:car_classes.Fleet):
    """Define car from terminal add remove it from a fleet."""
    fleet.print_whole_fleet()
    car = define_car_manually()
    print(f"Try to remove the following car: {car}")
    if fleet.remove_car_from_fleet(car):
        print(f"{car} is removed from fleet.")
    else:
        print(f"Car not found in {fleet}.")

def fuel_or_drive(car:car_classes.Car):
    """Randomly choosen from fuel or drive."""
    print("Now program is choosing randomly to drive or fuel the car.")
    r = random.randint(0,1)
    if r == 0:
        print("Fuel is chosen.")
        print("Program generates amount of fuel...")
        r = random.randint(0,1)
        if car.refuel(r):
            print(f"Refuel with {r} percentage happened.")
    else:
        print("Driving is chosen.")
        print("Program generates amount of kilometers...")
        r = random.randint(0,1000)
        if car.drive(r):
            print(f"Driving {r} kilometers happened.")

def summarize_driving_distance(fleet:car_classes.Fleet):
    """Summarize the every car's miles data in the whole fleet"""
    print(f"Total amount of miles in the whole fleet: {fleet.summarize_miles_in_whole_fleet()} kilometers.")

def input_brand_model_year():
    print("Please identify a car:")
    brand = input("Brand: ")
    model = input("Model: ")
    try:
        year = int(input("Year: "))
    except ValueError as e:
        print(f"Year has to be integer! {e}")
    else:
        return brand,model,year

def drive_manually(fleet:car_classes.Fleet):
    """Drive a car with x kilometers. car and x is user input."""
    print("Driving.")
    brand,model,year = input_brand_model_year()
    for car in fleet.cars_in_fleet:
        if car.brand == brand and car.model == model and car.year == year:
            print("Car found in fleet.")
            km = float(input("How many kilometers would drive?"))
            if car.drive(km):
                print(f"Driving {km} kilometers happened.")
            return True
    print("Car is not found in database.")
    return False

def fuel_manually(fleet:car_classes.Fleet):
    """Refuel a car with x percentage. x is user input."""
    print("Refuel.")
    brand,model,year = input_brand_model_year()
    for car in fleet.cars_in_fleet:
        if car.brand == brand and car.model == model and car.year == year:
            print("Car found in fleet.")
            percentage = float(input("How many percentage would you refuel?"))
            if car.refuel(percentage):
                print(f"Refuel with {percentage} percentage happened.")
            return True
    print("Car is not found in database.")
    return False

def randomly_executed_program(fleet:car_classes.Fleet):
    """Instead of waiting for user input program generates random numbers for execution. 
    Only one point where user has to interact: how many cars data would manipulate?
    Program randomly choose to fuel or drive with randomly genearted numbers.
    TODO: in the beginning fuel is full, so refuel can't happen."""
    fleet.print_whole_fleet()
    while True:
        try:
            input_car_number = int(input("How many cars would you like to manipulate (driving/fueling)?"))
        except ValueError as e:
            print(f"Input must be integer: {e}")
        except Exception as e:
            print(f"Exception happened during input value processing: {e}")
        else:
            if input_car_number > fleet.number_of_cars or input_car_number < 0:
                raise car_classes.UserDefineError("Input value is incorrect based on car numbers.")
            print(f"Now program is choosing {input_car_number} cars.")
            break
    random_list = []
    for idx,x in enumerate(range(input_car_number),1):
        print(f"{idx}. car manipulation is starting.")
        print("Now program choosing random car(s)...")
        # ensure to choose different cars from list
        while True:
            r = random.randint(0,fleet.number_of_cars-1)
            can_append = True
            for y in random_list:
                if y == r:
                    can_append = False
            if can_append:
                random_list.append(r)
                print(f"Selected car is: {fleet.cars_in_fleet[r]}")
                fuel_or_drive(fleet.cars_in_fleet[r])
                break
    fleet.print_whole_fleet()
    summarize_driving_distance(fleet)

def menu():
    print("You can choose from the following items:")
    print("1.\t Print whole fleet")
    print("2.\t Execute program with randomly generated fuel/driving")
    print("3.\t Add car to fleet")
    print("4.\t Remove car from fleet")
    print("5.\t Drive")
    print("6.\t Fuel")
    print("7.\t Summarize distance")
    print("8.\t Exit from program")

def user_input():
    while True:
        try:
            user_input=int(input("Please add one menu item between 1 and 8: "))
        except ValueError as e:
            print(f"Input is not integer: {e}")
        except Exception as e:
            print(f"Unxpected event happened during user input: {e}")
        else:
            if user_input < 1 or user_input > 8:
                print("Incorrect. Input has to be between 1 and 8!")
            else:
                print("Valid input.")
                break
    return user_input

def selected_menu(fleet:car_classes.Fleet):
    while True:
        menu()
        n = user_input()
        match n:
            case 1:
                fleet.print_whole_fleet()
            case 2:
                randomly_executed_program(fleet)
            case 3:
                add_car_to_fleet_manually(fleet)
            case 4:
                remove_car_manually(fleet)
            case 5:
                drive_manually(fleet)
            case 6:
                fuel_manually(fleet)
            case 7:
                summarize_driving_distance(fleet)
            case 8:
                print("Program is exited.")
                exit()
                break

def define_initial_input_for_program():
    cars = input_cars_from_file()
    fleet_1 = car_classes.Fleet("BestMax Car Fleet")
    print(f"Welcome at {fleet_1.name} company!")
    for car in cars:
        fleet_1.add_car_to_fleet(car)
    return fleet_1
    
if __name__ == "__main__":
    fleet1 = define_initial_input_for_program()
    selected_menu(fleet1)