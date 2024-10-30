city = str(input("What is the name of the city? Write your answer here: ")).title().strip()
rental_fee = int(input("How much is the rental fee? Write your answer here using only numbers: "))

if city in ["New York","San Francisco"] and (rental_fee < 4000):
    print(f"You can rent an apartment in {city} for {rental_fee}$.")
elif city == "Chicago":
    print(f"You found an apartment in your ideal city, in {city} for {rental_fee}$")  
elif city == "Washington":
    print(f"You hate {city} and you don't want to live there.")  
elif rental_fee < 3000:
    print(f"You can rent an apartment in {city} for {rental_fee}$.")
else:
    print(f"The apartment does not suits your needs. Please search another one.")
