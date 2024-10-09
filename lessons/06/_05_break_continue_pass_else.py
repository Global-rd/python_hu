#BREAK
attempts = 0
while attempts < 3:
    password = input("Enter your password:")
    if password == "secret":
        print("Access granted")
        break
    else:
        print("Wrong password, try again.")
    attempts += 1
else:
    print("Reached may tries, try tomorrow")


#CONTINUE

number = 0

while number < 10:
    number += 1
    if number % 2 == 0:
        continue
    print(f"Processing number {number}")


#PASS
numbers = []

for num in numbers:
    pass