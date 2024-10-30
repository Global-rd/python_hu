# mire jók a function-ök?
# - kód újra hasznosítás
# - a rendezettség fokozása
# - "separation of concerns" - különböző feladatok function-ökre bontása
# dolgok amiket érdemes betartani
# DRY: Don't Repeat Yourself -> repetitív logika absztrakciója function-ökkel
# Single Rensponsibility Principle -> egy function kizálrólag egy feladatért legyen felelős
# Kerüljük el a mutable object-eket default argumentekként!

#bad example:

name_1 = "Alice"
name_2 = "John"
name_3 = "Steve"
print(f"Hello {name_1}, welcome home!")
print(f"Hello {name_2}, welcome home!")
print(f"Hello {name_3}, welcome home!")

print("+------------------------")
#good example:
def greet_user(name):
    print(f"Hello {name}, welcome home!")

greet_user(name_1)
greet_user(name_2)
greet_user(name_3)


#for loop
print("---------------")
names = ["Alice", "John", "Steve"]
for name in names:
    greet_user(name)