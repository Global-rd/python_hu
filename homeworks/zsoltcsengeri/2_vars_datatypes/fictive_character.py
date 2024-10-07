#  1 Variables, user input, string methods, type conversion, f-string

# Asking user for input
name = input("Please give me the name of the character: ").strip().capitalize()


# Convert age to integer and calculate age in days
age = int(input("Please give me the age of the character: "))
age_in_days = age * 365

# Convert Python experience to integer
python_experience_in_years = int(input(
    "Please give me the Python experience of the character in years: "
))

# Displaying the entered information
print(
    f"My character is {age_in_days} days old. His/her name is {
        name} and he/she has {python_experience_in_years} years of Python experience."
)

# Extra challenge
# Asking user for input
wannabe_pro_python_user = input(
    "Do you want your character to be a professional Python user? yes/no ").strip().lower()


# Condition in a ternary operator
answer_outcome = "wants" if wannabe_pro_python_user == "yes" else "doesn't want"
# print(answer_outcome)
print(
    f"My character is {age_in_days} days old. His/her name is {
        name} and he/she has {python_experience_in_years} years of Python experience. He/she {answer_outcome} to become a professional Python programmer."
)
