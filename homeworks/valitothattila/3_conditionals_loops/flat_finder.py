print("---------------------Sarah lakást keres----------------------")

City_Name = input("Kérlek írd be a város nevét: ").strip().lower()
Rental_cost = 0
forbidden_city = False  # utólag hozzáadva, washingtonnál egyszerübb szöveg miatt

if City_Name != "washington":
    Rental_cost = int(input("Kérlek add meg a lakbért (USD): "))
    if City_Name != "chicago":
        if (City_Name == "new york" or City_Name == "san fransisco"):
           if Rental_cost < 4000 : 
               rental_condition = True # New York és San Fransisco kevesebb mint 4000 USD
           else:
               rental_condition = False # New York és San Fransisco drágább mint 4000 USD
        else:
            if Rental_cost <= 3000 : 
               rental_condition = True   # Ha nem New York és nem San Fransisco és kevesebb mint 3000 USD   
            else:
                rental_condition = False # Ha nem New York és nem San Fransisco és több mint 3000 USD
    else:
        rental_condition = True # Chicagó nem számít mennyibe kerül
   
else:
    rental_condition = False # Washington nem megfelelő
    forbidden_city = True
"----------------------------- Válaszok megfogalmazása-----------------------------------"
if rental_condition == True:
     print(f"{City_Name} város, és {Rental_cost} USD lakbér megfelel Sarah igényeinek!")      
else:
    if rental_condition == False and forbidden_city == False:
        print(f"{City_Name} város, és {Rental_cost} USD lakbér nem felel meg Sarah igényeinek!")
    else:    
        if rental_condition == False and forbidden_city == True:
            print(f"{City_Name} város, nem felel meg Sarah igényeinek!")
    


