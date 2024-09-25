#VÁLTOZÓK

name = "Jim"
age = 25

print(age)
age = 25 + 1
print(age)

camelCaseVariableName = "" #BAD PRACTICE PYTHON-BAN
snake_case_variable_name = "" #GOOD PRACTICE 

#KONSTANSOK
PI = 3.14
MAX_ROUNDS = 3

# dynamically typed / dinamikus típusosság
number = 10
number = "dog"
print(number)

#pointers
print("-----------")
my_var = 15
print(id(my_var))

my_var2 = 15
print(id(my_var2))

x = 5
y = x #5

print(id(x))
print(id(y))

x = 10

print(x)
print(y)

print(id(x))
print(id(y))

#GARBAGE COLLECTION
x = 1000
x = 2000 # 1000 got deleted from memory