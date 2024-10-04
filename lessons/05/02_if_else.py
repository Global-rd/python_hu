#syntax

condition = True

if condition == True:
    print("The condition is true.")
else:
    print("The condition is false.")


# truthy-falsy értékek

if condition:
    print("The condition is true.")
else:
    print("The condition is false.")


number = 0

if number:
    print(f"The value of 'a' is other than 0: {number}")
else:
    print(f"The value of 'a' is 0: {number}")

numbers = []

print(bool(numbers))

if numbers:
    print("The list has elements")
else:
    print("The list is empty")


#if-elif-else using arithmetic operators:
print("--------------------------")
number = 10

if number == 10:
    print("The number is 10")
elif number == 13:
    print("The number is 13")
elif number == 14:
    print("The number is 14")
else:
    print(f"The number is something else: {number}")


#if-elif-else using membership and logical operators:
print("--------------------------")

fruits = ["raspberry", "banana", "cherry", "watermelon"]

if "raspberry" in fruits:
    print("raspberry is present in fruits")

if "raspberry" in fruits or "banana" in fruits:
    print("either of the 2 is present")

if "raspberry" in fruits and "banana" not in fruits:
    print("raspberry in, banana not")

#identity operator

a = 1
b = 2

if a is b:
    print("The objects are the same")

c = 3
#combining multiple operators

if (a is not b and c == 3 and ("cherry" in fruits or "elderflower" in fruits)):
    print("Everything is OK")