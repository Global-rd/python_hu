# Extra homework - Nagy Norbert
from pprint import pprint

films = ["alien", "it", "amelie csodas elete", "hallo, hallo", "csengetett mylord"]

# define title of film
while True:
    film = input("Please enter title of film: ").strip().lower()
    if film not in films:
        print("Film is not found. Please try again!")
    else:
        break

cinema_matrix = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]
]

def print_cinema():
    """Print all places in cinema."""
    for id, row in enumerate(cinema_matrix,1):
        print("-----------------")
        for seat_id, seat in enumerate(row,1):
            print(f"{id}. row {seat_id}. seat: {seat}")

while True:
    ticket_num = int(input("How many tickets would you like to buy?"))
    if ticket_num < 1:
        print("Invalid tiket number, try again!")
    else:
        break

max_row = 4
max_column = 4

def choose_row():
    """Choose one valid row."""
    while True:
        input_row = int(input("Please add in which row would you sit:"))
        row = input_row - 1
        if row < 0 or row > max_row:
            print(f"Invalid row, it must be [1..{max_row+1}]")
        else:
            break
    
    return row 

def choose_column():
    """Choose one valid column."""
    while True:
        input_column = int(input("Please add in which column would you like to sit:"))
        column = input_column - 1
        if column < 0 or column > max_column:
            print(f"Invalid column, it must be [1..{max_column+1}]")
        else:
             break
    
    return column


def reserve_seat(x_row,y_col):
    """Reserve a seat, set value from 0 to 1."""    
    if cinema_matrix[x_row][y_col] == 0:
        cinema_matrix[x_row][y_col] = 1
        success_reservation = True
    else:
        success_reservation = False

    return success_reservation


print("Cinema before reservation:")
print_cinema()

for i in range(ticket_num):
    actual_row_num = choose_row()
    actual_col_num = choose_column()
    reserved = reserve_seat(actual_row_num,actual_col_num)
    if reserved: 
        print(f"Place reserved in {actual_row_num+1}.row, {actual_col_num+1}.column.")
    else:
        print("This place is already reserved.")

print("Cinema after reservation:")
print_cinema()







