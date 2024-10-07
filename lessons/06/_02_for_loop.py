import time

#for loop with lists
songs = ["I'm a barbie girl", "8 óra munka", "Autó egy szerpentinen", "Heavy is the crown"]

for song in songs:
    print(f"Playing {song}")
    #time.sleep(1)


print("------------------------")
#for loop with string
name = "Steve Jobs"
for char in name:
    print(char)

print("------------------------")
#for loop with dictionaries

student = {
    "name": "John",
    "age": 20,
    "grades": [4,5,5],
    "major": "Computer Science",
    "is_active": True,
}

#both keys and values
for k,v in student.items():
    print(f"Key: {k}, value: {v}")

#just keys
for k in student.keys():
    print(k)

#just values
for v in student.values():
    print(v)

#range
for id in range(5):
    print(id)