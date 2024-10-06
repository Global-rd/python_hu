



name_new = input("Name? ")
name_new = name_new.strip().upper()
age_new =int(input("Age? "))
age_day = int(age_new * 365.25)
python_exp = int(input("Python experience in years? "))
professional_n = input("Professional Python experience? ")
professional_n = professional_n.upper()
want_prof="wants" if professional_n == "YES" else "does not want"
print(f"My character is {age_day} days old. His/her name {name_new} and he/she has {python_exp} years experience. He/she {want_prof} to be Python developer.")


