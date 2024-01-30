#calc divisibility
num = int(input("Enter a Number: "))
if num % 5 == 0 or num % 7 == 0 or num % 11 == 0 or num % 2 == 0:
    if num % 5 == 0:
        print("The number is divisible by 5")
    else:
        print("Not divisible by 5")
    if num % 7 == 0:
        print("The number is divisible by 7")
    else:
        print("Not divisible by 7")
    if num % 5 == 0:
        print("The number is divisible by 11")
    else:
        print("Not divisible by 11")
    if num % 2 == 0:
        print("The number is divisible by 2")
    else:
        print("Not divisible by 2")
else:
    print("Not divisible by either")
