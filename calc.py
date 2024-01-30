print("Simple Calculator")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("\nChoose operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
print("5. Modulus (%)")
print("6. Exponents (^)")
print("7. Floor Division (//)")

print("Enter operator choice")
choice = input("Enter choice (1-7): ")

if choice == '1':
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
if choice == '2':
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
if choice == '3':
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
if choice == '4':
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Cannot divide by zero.")
if choice == '5':
    result = num1 % num2
    print(f"{num1} % {num2} = {result}")
if choice == '6':
    result = num1 ** num2
    print(f"{num1} ^ {num2} = {result}")
if choice == '7':
    if num2 != 0:
        result = num1 // num2
        print(f"{num1} // {num2} = {result}")
    else:
        print("Error: Cannot perform floor division by zero.")
if choice not in ['1', '2', '3', '4', '5', '6', '7']:
    print("Invalid choice. Please enter a number between 1 and 7.")
