def calculator():
    print("Calculator")
    print("Enter two numbers:")
    
    try:
        num1 = float(input("First number: "))
        num2 = float(input("Second number: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return

    print("Choose an operation: Addition(+),Subtraction(-),Multiplication(*), Division(/)")
    operation = input("Operation: ")

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 == 0:
            print("Error! Division by zero is not allowed.")
            return
        result = num1 / num2
    else:
        print("Invalid operation! Please choose a valid operator.")
        return

    print(f"Result: {result}")

calculator()
