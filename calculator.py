num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("Choose operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
choice = input("Enter your choice (+, -, *, /): ")
if choice == '+':
    result = num1 + num2
    print("Result =", result)
elif choice == '-':
    result = num1 - num2
    print("Result =", result)
elif choice == '*':
    result = num1 * num2
    print("Result =", result)
elif choice == '/':
    if num2 != 0:
        result = num1 / num2
        print("Result =", result)
    else:
        print("Error! Division by zero is not allowed.")
else:
    print("Invalid operation choice")