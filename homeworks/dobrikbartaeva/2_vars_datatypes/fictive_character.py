name = (input("Enter your name: ")).upper().strip() 
#mit jelent a nagy betűvel? az egész nagybetű? Én annak vettem... Vagy nagy kezdőbetű? mert akkor .capitalize() a .upper() helyett

age_years = int(input("Enter your age (in years): "))
age_days = age_years * 365
py_experience_years = int(input("Enter your Python experience in years: "))

prof_ambitions = (input("Would you like to be a professional? (yes/no): ")).lower().strip()
prof_ambitions_text = "He/she wants to be a Python developer!" if prof_ambitions == "yes" else "He/she does not want to be a Python developer!"

# Mivel nem "days old"-ot írt a feladat szövege, ezért én sima "old"-ot írok:
print(f"My character is {age_days} old. His/her name is {name} and he/she has {py_experience_years} years experience. {prof_ambitions_text}")
