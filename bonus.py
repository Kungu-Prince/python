#calculate amount of salary to be given to an employee
print("Amount of salary")
salary = float(input("Enter your salary: "))
print("Years in service")
years = int(input("Enter the number of years of service in the company: "))
if years >10:
    bonus = 0.1*salary
    net_salary = bonus + salary
    print("Bonus is: ", bonus)
    print("net_salary is: ", net_salary)
elif years >=6 and years <=10:
    bonus = 0.08*salary
    net_salary = bonus + salary
    print("Bonus is: ", bonus)
    print("net_salary is: ", net_salary)
elif years <6:
    bonus = 0.06*salary
    net_salary = bonus + salary
    print("Bonus is: ", bonus)
    print("net_salary is: ", net_salary)
else:
    print("Not applicable")