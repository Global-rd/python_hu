full_name = input("Please enter your full name.").title().strip()           #BEKÉRJÜK A TELJES NEVET.

age = int(input("Please enter your age."))                                       #BEKÉRJÜK A KORÁT.

experince_in_python = int(input("Please enter your experience with python in years."))    #BEKÉRJÜK, HOGY HÁNY ÉV TAPSZTALATA VAN PYTHON-BAN.

age_in_days = age * 365              #MEGHATÁROZZUK, HOGY A MEGADOTT KOR AZ MENNYI NAPOKBAN KIFEJEZVE.



print(f"""My character's name is {full_name}.
He/she is {age} years old, which is {age_in_days}.
He/she has {experince_in_python} year(s) of experience in python.""")

