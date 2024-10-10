from os import system
system("cls")

def city_to_live (city, rent):
    if city == "Washington" :
        return f'Try another place, as you hate Washington'
    if city == "Chicago" :
        return  f'You can live in Chicago!'
    if rent > budget_limit(city) :
        return  f'This is above your budget.'
    else :
        return f'You can live in {city} for {rent} USD.'


def budget_limit (city) :
    if city == "New York" or city == "San Francisco" :
       return 4000
    else :
       return 3000
    
city = input("Give me the city's name:")
rent = int(input("Give me the rent amount:"))

print(city_to_live(city, rent))



"""
For esting purpose

city_to_live("New York", 3900)
city_to_live("Chicago", 8000)
city_to_live("Washington", 3900)
city_to_live("Oslo", 3900)

"""    




