fruit = "apple"

print(type(fruit))
print(isinstance(fruit, str))

#type conversion / típus konverzió

num_int = 10
num_float = 10.5

result = num_int * num_float
print(result)

age = "13"
print(age*10)
result = int(age) / 2
print(result)

age = int(input("How old are you?"))

age: int = 0
# truthy -falsy értékek

print(bool(1))
print(bool(0))
print(bool(""))
print(bool("apple"))

# egyéb típuskonverzióra használható függvények:
float()
str()
int()
bool()
