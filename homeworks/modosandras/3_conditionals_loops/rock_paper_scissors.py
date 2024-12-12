pont_1 = 0
pont_2 = 0

while True:
    korok_szama = int(input("Körök száma: "))
    if korok_szama %2 == 0:
        print("Csak páratlan szám elfogadható!")
    else:
        break

for aktualis_kor in range(korok_szama):
    print(f"---- {aktualis_kor + 1}/{korok_szama} kör ----")
    while True:
        while True:
            valasz = input("1. játékos válasza: ")
            if valasz in ["rock", "paper", "scissors"]:
                valasz_1 = valasz
                break
            else:
                print("Érvénytelen válasz! Érvényes válaszok: rock, paper, scissors")

        while True:
            valasz = input("2. játékos válasza: ")
            if valasz in ["rock", "paper", "scissors"]:
                valasz_2 = valasz
                break
            else:
                print("Érvénytelen válasz! Érvényes válaszok: rock, paper, scissors")

        if valasz_1 == valasz_2:
            print("Azonosak a válaszok, a kört újrakezdjük!")
        else:
            break

    if valasz_1 == "rock":
        if valasz_2 == "paper":
            pont_2 += 1
        else:
            pont_1 += 1
    if valasz_1 == "paper":
        if valasz_2 == "scissors":
            pont_2 += 1
        else:
            pont_1 += 1
    if valasz_1 == "scissors":
        if valasz_2 == "rock":
            pont_2 += 1
        else:
            pont_1 += 1

print("=== A játéknak vége. ===")
print(f"1. játékos pontjai: {pont_1}")
print(f"2. játékos pontjai: {pont_2}")
print("=== Eredményhirdetés ===")

if pont_1 > pont_2:
    print(f"1. játékos nyert {pont_1} ponttal.")
else:
    print(f"2. játékos nyert {pont_2} ponttal.")