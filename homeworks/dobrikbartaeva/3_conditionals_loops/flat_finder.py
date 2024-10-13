name = "Sarah"
currency = "USD"

pref_city_limit = ["New York", "San Francisco"]
hated_city = ["Washington"] #nem szükségszerű a lista,de talán így könnyebb bővíteni később a kódot ha több várost utálnának 
pref_city_limitless =["Chicago"] #nem szükségszerű a lista,de talán így könnyebb bővíteni később a kódot ha több várost utálnának 

city = input("Please enter your preferred city: ").strip().lower().title()

if city in hated_city:
    willing_to_move = "not "
    rent_amount = "any money"
    currency =""
elif city in pref_city_limitless:
    willing_to_move = ""
    rent_amount = "any amount"
    currency =""
else: 
    rent_amount=(int(input(f"Please enter max rent amount {currency}: ")))
    if city in pref_city_limit and rent_amount <= 4000:
        willing_to_move = ""
    elif rent_amount <= 3000:
        willing_to_move = ""
    else:
        willing_to_move = "not "    

print(f"Sarah is {willing_to_move}happy to move to {city} for {rent_amount}{currency}.")

