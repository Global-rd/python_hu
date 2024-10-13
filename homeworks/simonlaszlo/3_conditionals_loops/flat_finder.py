
cityes=("New York","San Francisco","Washington","Chichago")
city_name,city_cost=input("Please enter the city name and the monthly fee of the sublet, separated by commas! ").split(",")
city_name=city_name.strip().title()
city_cost=int(city_cost)
print(f"The City name is: {city_name}, monthly price: {city_cost}")

if (city_name==cityes[0]  or city_name==cityes[1]) and city_cost<4000 :
    city_print=""
elif city_name==cityes[2] :
    city_print="not "
elif city_name==cityes[3] :
    city_print=""
elif city_cost<=3000 :
    city_print=""
else :
    city_print="not "

print(f"The sublet is {city_print}suitable for moving in!")






