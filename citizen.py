#check for citizenship for East AFrica community
age = int(input("Please enter your age :"))
nationality = input("Enter your Nationality:")
East_African_countries = ("Kenya", "Uganda", "Tanzania")
if age>= 18 and nationality == "Kenya" or nationality == "Tanzania" or nationality == "Uganda":
    print("You are Eligible to vote")
else:
    print("Not Eligible")