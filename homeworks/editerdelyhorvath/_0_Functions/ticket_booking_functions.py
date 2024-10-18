
'''
Definiciók a Ticket booking file-hoz

'''

def print_seating_area(seating_area):
    '''Print the Seating Area from a list in list matrix'''

    for row_id, row in enumerate(seating_area, 1):
        print(f"Row {row_id}: ", end="      ")
        for seat_id, seat in enumerate(row, 1):
            if seat == 0:
                print(f"    Seat {seat_id} -\033[32m Available\033[0m", end="  ")  # with green "Available"
            elif seat == 2:
                print(f"    Seat {seat_id} -\033[36m Selected \033[0m", end="  ")  # with cian "Selected"
            elif seat == 3:
                print(f"    Seat {seat_id} -\033[34m Bought   \033[0m", end="  ")  # with blue "Selected"    
            else:
                print(f"    Seat {seat_id} -\033[31m Booked   \033[0m", end="  ")     # with red "Booked"
        print()  # new row for the next row

def is_seat_available(seating_area, row, seat):
    ''' check if the seat is available or not'''
    if seating_area[row - 1][seat - 1] == 0:
        return True
    else:
        return False


def update_seating_area_booked(seating_area):
    '''update the bought seats to booked'''
    for row in range(len(seating_area)):
        for seat in range(len(seating_area[row])):
            if seating_area[row][seat] == 3:
                seating_area[row][seat] = 1

def update_seating_area_bought(seating_area):
    '''update the selected seats to bought'''
    for row in range(len(seating_area)):
        for seat in range(len(seating_area[row])):
            if seating_area[row][seat] == 2:
                seating_area[row][seat] = 3

def book_seat(temp_seating_area, ticket_number):
    """Ask the user to select a row and seat, and book it if available."""
    while True:
        print(f"Please enter the parameters of the ticket {ticket_number}:")
        selected_row = int(input("Enter the selected row (number): ").strip())
        selected_seat = int(input("Enter the selected seat (number): ").strip())
        
        # Check if the seat is available or not
        if is_seat_available(temp_seating_area, selected_row, selected_seat):
            temp_seating_area[selected_row - 1][selected_seat - 1] = 2  # booking
            break  # Exit the while loop when a valid seat is chosen
        else:
            print("The selected seat is already booked. Please choose a different seat.")
