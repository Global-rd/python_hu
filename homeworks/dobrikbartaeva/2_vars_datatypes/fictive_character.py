name = (input("Enter your name: ")).capitalize().strip() 
#mit jelent a nagy betűvel? az egész nagybetű? Én annak vettem... Vagy nagy kezdőbetű? mert akkor .capitalize() a .upper() helyett

age_years = int(input("Enter your age (in years): "))
age_days = age_years * 365
py_experience_years = int(input("Enter your Python experience in years: "))

prof_ambitions = (input("Would you like to be a professional? (yes/no): ")).lower().strip()
prof_ambitions_text = "wants" if prof_ambitions == "yes" else "does not want"

# Mivel nem "days old"-ot írt a feladat szövege, ezért én sima "old"-ot írok:
print(f"My character is {age_days} old. His/her name is {name} and he/she has {py_experience_years} years experience. He/she {prof_ambitions_text} to be a Python developer!")