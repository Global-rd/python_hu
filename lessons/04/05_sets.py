original_numbers = {1,2,3,4,5}
new_numbers = {4,5,6,7}
print(id(original_numbers))
original_numbers.update(new_numbers)
print(original_numbers)
print(id(original_numbers))


numbers_list = [0,0,0,0,0,0,0,1,1,1,1,1,2,2,2,2]
numbers_list = list(set(numbers_list))
print(numbers_list)


# methods

original_numbers.add(1)
original_numbers.remove(1)

original_numbers = {1,2,3,4,5}
new_numbers = {4,5,6,7}

intersection = original_numbers.intersection(new_numbers)
print(intersection)

# frozenset
my_set = frozenset([1,2,3])
print(my_set)