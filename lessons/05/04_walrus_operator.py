#without walrus operator

items = ["apple", "raspberry", "banana", "cherry"]
treshold = 3

length = len(items)
print(length)

if length > treshold:
    print(f"The list has {length} items, which is greater than {treshold}")

#with walrus operator

if (length :=len(items)) > treshold:
    print(f"The list has {length} items, which is greater than {treshold}")

