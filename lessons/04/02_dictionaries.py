from pprint import pprint

student = {
    "name": "John",
    "age": 20,
    "grades": [4,5,5],
    "major": "Computer Science",
    "is_active": True,
}

pprint(student)

#accessing values / értékek elérése

print(student["age"])

print(student["grades"][-1])

#accesing keys

print(student.keys())
print(type(student.keys()))

#accessing values
print(student.values())
print(type(student.values()))


student["name"] = "John Hopkins"
pprint(student)

student["grades"].append(3)
pprint(student)

latest_grade = int(input("Grade: "))

us_grade_mapping = {
    5: "A",
    4: "B",
    3: "C",
    2: "D",
    1: "F"
}

us_grade = us_grade_mapping[latest_grade]
print(us_grade)