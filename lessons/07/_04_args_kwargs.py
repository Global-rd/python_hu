#ARBITRARY ARGUMENTS: *args

def sum_numbers(*args):
    return sum(args)


result = sum_numbers(1,2,3,4,5)
print(result)

result = sum_numbers(1,2)
print(result)


# ARBITRARY KEYWORD-ARGUMENTS

def describe_person(**kwargs):
    print(kwargs)
    print(type(kwargs))
    for k, v in kwargs.items():
        print(f"Key: {k}, Value: {v}")


describe_person(name="Steve", age=14, job="programmer")

#combining positional, default, args, kwargs

def introduce_person(name, age, *hobbies, country="Hungary", **additional_info):

    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Country: {country}")

    if hobbies:
        print("Hobbies:")
        for hobby in hobbies:
            print(f"  - {hobby}")

    if additional_info:
        print("Additional information:")
        for k,v in additional_info.items():
            print(f"   - {k} - {v}")


introduce_person("John",
                  15,
                 "hiking",
                 "reading",
                 "traveling",
                 country="Switzerland",
                 occupation = "Engineer",
                 has_pet=True)
