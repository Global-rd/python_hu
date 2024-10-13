# Schreiner Balázs ► 2_homework
name = input("Enter your name: ").strip().capitalize()
age = round(int(input ("Your age (years): "))*365.25)
python_experience_years = int(input ("Your Phyton experience (years): "))
#print (name)
#print (age)
#print (python_experience_years)
#print(type(age))

"""Extra:"""
python_want_to_be = input("Do you want to become a Python developer? (yes/no) ").strip().upper()

python_want_to_be = "want to become a Phyton developer." if python_want_to_be == "YES" else "don't want to be a Phyton developer."
#print (python_want_to_be)

print(f"Hi, {name}! You are {age} days old. You have {python_experience_years} year(s) experience as a Python developer. And You {python_want_to_be}")