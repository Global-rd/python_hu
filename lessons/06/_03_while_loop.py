while True:
    answer = input("Do you want to be a prof. python developer? yes/no")
    if answer in ["yes", "no"]:
        break

print("This is running after the while loop.")

#INFINITE LOOP / VÉGTELEN CIKLUS
#while True: 
#    print("infinite loop")

count = 0
while count < 5:
    print(count)
    count += 1

print("this will run after the loop")