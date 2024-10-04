# if number is divideable by 3 and 5: FizzBuzz
# if nummber is divideable by 3: Fizz
# if number is divideable by 5: Buzz
# else: number as a string

n = 1

if n % 3 == 0 and n % 5 == 0:
    print("FizzBuzz")
elif n % 3 == 0:
    print("Fizz")
elif n % 5 == 0:
    print("Buzz")
else:
    print(str(n))


#HELYTELEN!
if n % 3 == 0:
    print("Fizz")
elif n % 3 == 0 and n % 5 == 0:
    print("FizzBuzz")
elif n % 5 == 0:
    print("Buzz")
else:
    print(str(n))