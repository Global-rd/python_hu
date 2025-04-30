# to_do.py
import time
    
def add():
    print("1-es válasz")
    time.sleep(2)
    

def view():
    print("2-es válasz")
    time.sleep(2)

def remove():
    print("3-es válasz")
    time.sleep(2)

def display_menu():
    while True :
        print("  1. Add Task\n  2. View Tasks\n  3. Remove Task\n  4. Exit")    
        
        valasz = input("Válassz : ")
        
        if valasz == '1' :
            add()
        elif valasz == '2' :
            view()
        elif valasz == '3' :
            remove()
        elif valasz == '4' :
            print("Kilépés!")
            break    
        else : 
            print("Érvénytelen választás !")
            time.sleep(2)    

display_menu()
    