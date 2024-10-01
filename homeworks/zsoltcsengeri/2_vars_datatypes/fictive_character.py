# Asking user for input
name = input("Please give me the name of the character: ")
name = name.strip().capitalize()

# Convert age to integer and calculate age in days
age = int(input("Please give me the age of the character: "))
age_in_days = age * 365

# Convert Python experience to integer
python_experience_in_years = input(
    "Please give me the Python experience of the character in years: "
)

# Displaying the entered information
print(
    f"My character is {age_in_days} days old. His/her name is {name} and he/she has {python_experience_in_years} years of Python experience."
)
