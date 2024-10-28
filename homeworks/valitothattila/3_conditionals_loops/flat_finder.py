print("---------------------Sarah lakást keres----------------------")

city_name = input("Kérlek írd be a város nevét: ").strip().lower()
rental_cost = 0
forbidden_city = False  # utólag hozzáadva, washingtonnál egyszerübb szöveg miatt
if city_name != "washington":
    rental_cost = int(input("Kérlek add meg a lakbért (USD): "))
else:
    rental_condition = False # Washington nem megfelelő
    forbidden_city = True

if city_name == "chicago":
    rental_condition = True # Chicagó nem számít mennyibe kerül
elif (city_name == "new york" or city_name == "san fransisco") and rental_cost < 4000:
    rental_condition = True # New York és San Fransisco kevesebb mint 4000 USD
elif rental_cost <= 3000 : 
    rental_condition = True   # Ha nem New York és nem San Fransisco és kevesebb mint 3000 USD   
else:
    rental_condition = False # Ha nem New York és nem San Fransisco és több mint 3000 USD

#----------------------------- Válaszok megfogalmazása-----------------------------------
if rental_condition == True and forbidden_city == False:
    print(f"{city_name} város, és {rental_cost} USD lakbér megfelel Sarah igényeinek!")      
elif rental_condition == False and forbidden_city == False:
    print(f"{city_name} város, és {rental_cost} USD lakbér nem felel meg Sarah igényeinek!")
else:
    print(f"{city_name} város, nem felel meg Sarah igényeinek!")   


