
name_of_the_traveler = "Sarah"
city_name = input(f"Szia, kérlek add meg a várost ahova {
                  name_of_the_traveler} utazni szeretne:  ")
available_budget = int(input(f"Most kérlek add meg hogy, {
                       name_of_the_traveler} mennyit szán a havi albérletre (USD): "))
NY_and_SF_budget_limit = 4000
general_budget_limit = 3000

if city_name == "Washington":
    print(f"{name_of_the_traveler} nem szeretne {city_name}-ba költözni! ")
elif city_name == "Chicago":
    print(f"{name_of_the_traveler} annyira szereti {
          city_name}-t hogy bármi áron beköltözne")
# elif((available_budget < 4000) and (city_name == "New York" or city_name == "San Francisco")):
elif (city_name in ["New York", "San francisco"] and available_budget < NY_and_SF_budget_limit):
    print(f"{name_of_the_traveler} egyik kedvenc városa {city_name} és az ár is {
          NY_and_SF_budget_limit} USD alatt van így beköltözne  ")
elif (available_budget < general_budget_limit):
    print(f"{name_of_the_traveler} szívesen beköltözne {
          city_name}-be mivel az ára {general_budget_limit} alatt van")
else:
    print(f"{name_of_the_traveler} nem költözne {
          city_name}-ba/be mivel túlzottan drága")
