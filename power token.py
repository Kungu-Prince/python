#electric bill calculator
import math
def electric_bill(units, CustomerID, CustomerName):
    
    if  units >= 600: 
        bill = units * 2.00   
    elif units >= 400 and units <600:
        bill = units * 1.80
    elif units >= 200 and units <400:
        bill = units * 1.50
    elif units <= 199:
        bill = units * 1.20

    return bill

CustomerID = (input("Enter your customer id: "))
CustomerName = (input("Enter your name: "))
UnitConsumed = float(input("Enter units consumed: "))   
print(electric_bill(UnitConsumed, CustomerID, CustomerName))
