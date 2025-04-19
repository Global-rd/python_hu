#BEKÉRJÜK AZ INFORMÁCIÓT VÁROS + LAKBÉR:
apartment_location = input("please enter city!").title()
apartment_monthly_rent = int(input("please enter the monthly rent in USD!"))


#IF METÓDUS ARRA AZ ESETRE, HA A BEKÉRT ADAT MEGEGYEZIK NEW YORK VAGY SAN FRANSISCO-VAL ÉS AZ ÁRA KEVESEBB, MINT 4000 USD:
if apartment_location in ["New York", "San Fransisco"] and apartment_monthly_rent < 4000:
    print(f"""Sarah loves {apartment_location} 
and accepts the offer of {apartment_monthly_rent} USD / month!""")


#ELIF ALKALMAZÁSA ARRA AZ ESETRE, HA A MEGADOTT VÁROS WASHINGTON, EBBEN AZ ESETBEN SARAH BIZTOS NEM KÖLTÖZIK ODA.
elif apartment_location == "Washington":
    print(f"""Sarah hates {apartment_location} 
and doesn't want to live there no matter what!""")
    

#ELIF ALKALMAZÁSA ARRA AZ ESETRE, HA A MEGADOTT VÁROS CHICAGO, EBBEN AZ ESETBEN SARAH BIZTOS KÖLTÖZIK.
elif apartment_location == "Chicago":
    print(f"""Sarah always wanted to live in {apartment_location}, 
so she accept the offer of {apartment_monthly_rent} USD / month!""")


#ELSE ALKALMAZÁSA, AZ IF LEZÁRÁSÁHOZ, AMELYEN BELÜL EGY ÚJ IF TALÁLHATÓ.
#ÚJ IF FELDOLGOZZA AZT AZ ESETET, HOGY:
#           - EGYÉB VÁROS MINT A KORÁBBAN FELSOROLTAK,
#           - MI VAN AKKOR HA TÖBB, VAGY EGYENLŐ ÉS KEVESEBB A LAKBÉR, MINT 3000 USD.
#(tudom, hogyan lehet többsoros kommentet írni, de nekem így transzparensebb a színek miatt)
else:
    if apartment_monthly_rent <= 3000:
        print(f""""Sarah wants to move in to your apartment in {apartment_location} 
and accepts the offer of {apartment_monthly_rent} USD / month.""")
    else:
        print(f"""Sorry, but Sarah wants to live in an apartment, 
where the monthly rent is equal or under 3000 USD.""")

   
#MINDEN ESETBEN AZ F-STRING ALKALMAZÁSÁVAL KAPUNK EGY VÁLASZT, AMI AZ ADOTT FELTÉTELEKRE VONATKOZIK. 