#checking if someone is eligible to vote
age = int(input("Please enter your age :"))
Country = ("Kenya")
nationality = input("Enter your Nationality:")

if age>= 18 and nationality == "Kenyan":
    print("You are Eligible to vote")
else:
    print("Not Eligible")