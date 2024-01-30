#calc discount
cost = float(input("Enter the amount purchased :"))
if cost >= 1000:
    print("Discount is :", 0.05 * cost)
else:
    print("No Discount")
