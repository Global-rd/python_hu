'''
2. házi feladat

Feladat 1: Változók, user input, string metódusok, type conversion, 
f-string használata

+ Extra feladat (szorgalmi)
'''
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../_0_Functions')))

from terminal_clearer import clear_terminal


# Ask the user for input
name = input("Enter your name: ").strip().upper()
age_in_years = int(input("Enter your age (in years): ").strip())
python_exp_in_years = float(input("Enter your Python experience (in years): ").strip())  # allowing a fraction of a year - eg half a year

# EXTRA - Ask if the character wants to be a professional Python developer
wants_to_be_dev_input = input("Do you want to be a professional Python developer? (yes/no): ").strip().lower()

# Store the appropriate string based on the user's response
wants_to_be_dev = 'I am happy you want' if wants_to_be_dev_input == "yes" else 'I am sad that you do not want'

# Convert age to days (assuming 365 days per year)
age_in_days = age_in_years * 365

clear_terminal()

# Print the result using multi-line f-string
print(f"""
Your name is {name}, you are {age_in_days:.0f} days old and you have {python_exp_in_years} years of Python experience.
{wants_to_be_dev} to be a Python developer.\n\n
""")

'''
Megadott adatok:
Enter your name: Nyugton Malac
Enter your age (in years): 40
Enter your Python experience (in years): 0.6
Do you want to be a professional Python developer? (yes/no): yes

Enter után tiszta terminalban:
Your name is NYUGTON MALAC, you are 14600 days old and you has 0.6 years of Python experience.
I am happy you want to be a Python developer.

két sortöréssel az átláthatóság miatt.

'''