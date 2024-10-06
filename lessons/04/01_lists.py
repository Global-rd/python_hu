
letters = ["a", "a", "a", "b", "c"]
print(letters)
mixed_type_list = ["a", 123, 123.5, None, True]
print(mixed_type_list)

letters = []
letters_2 = list()
print(letters)
print(letters_2)

numbers = list(range(10))
print(numbers)

#indexing

names = ["Sarah", "Jim", "Dexter"]
print(names[:2])

#changing items / elemek megváltoztatása

names[0] = "Steve"
print(names)

names[:2] = ["Maria", "Kyle"]
print(names)

#inserting more
names[1:2] = ["Timmy", "Jeremy"]
print(names)

#inserting less
names[1:3] = ["Timy"]
print(names)

#names[1:3] = "TimyTimy" #ne így!
#print(names)


#methods

names.append("Cathlyn")
print(names)

#names.append(["Zeno", "Paula"])
#print(names)

names.extend(["Zeno", "Paula"])
print(names)

names.insert(0, "Jimmy")
print(names)

#remove by item value
names.remove("Jimmy")

#remove by item index

names.pop(1)
print(names)

del names[1]

# full deletion of all items from the list
names.clear()


chocolates = input("Give me your 3 favourite chocolates separated by a comma!")
print(chocolates)
print(type(chocolates))

chocolates_list = chocolates.split(",")
print(chocolates_list)
chocolates_list.append("mars")
print(len(chocolates_list))