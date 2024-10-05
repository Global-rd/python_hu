full_name = (input("Please enter your full name."))         #BEKÉRJÜK A TELJES NEVET.

age = (str(input("Please enter your age.")))                #BEKÉRJÜK A KORÁT.

experince_in_python = (str(input("Please enter your experience with python in years.")))    #BEKÉRJÜK, HOGY HÁNY ÉV TAPSZTALATA VAN PYTHON-BAN.

age_in_days = int((age)) * 365              #MEGHATÁROZZUK, HOGY A MEGADOTT KOR AZ MENNYI NAPOKBAN KIFEJEZVE.



print("My character's name is " + (full_name.title().strip()) + ".")
print("He is " + (age) + " years old, which is " + str((age_in_days)) + " days.")
print("He has " + (experince_in_python) + " year(s) of experience in python.")

