# FILE HANDLING WITHOUT CONTEXT MANAGERS:
import os
print(os.getcwd())

file = open("lessons/08/sample.txt", "w") #relative path

try:
    file.write("This is some sample text")
finally:
    file.close()

# WITH CONTEXT MANAGERS:

with open("lessons/08/sample.txt", "w") as file:
    file.write("This is some sample text from the CM.\n")

# WITH CONTEXT MANAGERS - APPEND:

with open("lessons/08/sample.txt", "a") as file:
    file.write("This is some sample text from the CM. \n")

# FILE HANLING: READING A FILE:

print("-----------------")
with open("lessons/08/sample.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())


# USING GENERATOR TO READ A FILE:
print("-------------------------------")

def read_file_line_by_line(file_path):
    with open(file_path, "r") as file:
        for line in file:
            yield line

file_path = "lessons/08/sample.txt"
gen = read_file_line_by_line(file_path=file_path)
print(next(gen))
print(next(gen))

for line in read_file_line_by_line(file_path=file_path):
    print(line)