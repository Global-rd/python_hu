# len() 
fruit = "raspberry"
fruit_length = len(fruit)
print(type(fruit_length))

# concatenation / string összefűzés
first_name = "Istvan Gabor"
last_name = "Nagy"

full_name = first_name + " " + last_name
print(full_name)
introduction = "My name is " + first_name + " " + last_name + "."
print(introduction)

# interpolated string / f-stringek
introduction = f"My name is {first_name} {last_name}."
print(introduction)


# indexing, slicing
print(fruit)
print(fruit[0])
print(fruit[1])
print(fruit[2])
print(fruit[-1])

print(fruit[1:3]) # 1. index: inclusive, 2. index: exclusive
print(fruit[3:])
print(fruit[-2:])
print(fruit[-1::-1])

# string metódusok

#metódus: az amit az objektum tud csinálni
#attribútum: ami jellemzi az objektumot

# objektum: kutya 
# metódus: ugat, evés, ülés, játék stb.
# attribútum: kor, fajta, név stb.

print(fruit)
print(fruit.capitalize())
print(fruit.upper())
print(fruit.title())

fruit = " apple  "
fruit = fruit.strip()
print(fruit)

replaced_char_fruit = fruit.replace("a", "b")
print(replaced_char_fruit)

p_index = fruit.find("p")
print(p_index)

fruit = "      apple      "
fruit = fruit.strip().capitalize() # method chaining.
print(fruit)