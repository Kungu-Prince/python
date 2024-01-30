#loan application
age = int(input("Please enter your age :"))
salary = float(input("Enter your annual income :"))  
if age >= 21 and salary >= 21000:
    print("Congratulations! You qualify for a loan👍")
else:
    print("Unfortunately, we are unable to offer you a loan at this time😒")