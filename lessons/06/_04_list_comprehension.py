import time

numbers = [1, 2, 3, 4, 5]

#without list comprehension
squared_numbers = []
for num in numbers:
    squared_numbers.append(num ** 2)

print(squared_numbers)

#with list comprehension

squared_numbers = [num ** 2 for num in numbers]
print(squared_numbers)

#without list comprehension

even_squares = []

for num in numbers:
    if num % 2 == 0:
        even_squares.append(num ** 2)

print(even_squares)

#with list comprehension

even_squares = [num ** 2 for num in numbers if num % 2 == 0]
print(even_squares)

new_list = ["even" if num % 2 == 0 else "odd" for num in numbers]
print(new_list)


numbers = range(1, 1000000)

#for loop
start = time.time()
print(start)
squares_loop = []
for num in numbers:
    squares_loop.append(num ** 2)
print(f"For loop: {time.time() - start}")

#list comprehension
start = time.time()
squares_comprehension = [num ** 2 for num in numbers]
print(f"Comprehension: {time.time() - start}")