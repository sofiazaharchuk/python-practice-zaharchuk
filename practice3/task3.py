print("Sofia Zaharchuk, IT-32")

first_number = float(input("First number: "))
operation = input("Operation (+, -, *, /, //, %, **): ")
second_number = float(input("Second number: "))

if operation == "+":
    result = first_number + second_number
elif operation == "-":
    result = first_number - second_number
elif operation == "*":
    result = first_number * second_number
elif operation == "/":
    if second_number == 0:
        result = None
        print("Error: division by zero")
    else:
        result = first_number / second_number
elif operation == "//":
    if second_number == 0:
        result = None
        print("Error: division by zero")
    else:
        result = first_number // second_number
elif operation == "%":
    if second_number == 0:
        result = None
        print("Error: division by zero")
    else:
        result = first_number % second_number
elif operation == "**":
    result = first_number ** second_number
else:
    result = None
    print(f"Error: unknown operation '{operation}'")

if result is not None:
    print(f"{first_number} {operation} {second_number} = {result:.4f}")
