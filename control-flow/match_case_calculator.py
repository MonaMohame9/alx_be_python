# match_case_calculator.py

# طلب الأرقام من المستخدم
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# طلب العملية
operation = input("Choose the operation (+, -, *, /): ")

# استخدام Match Case لتنفيذ العملية
match operation:
    case "+":
        result = num1 + num2
        print(f"The result is {result}")
    case "-":
        result = num1 - num2
        print(f"The result is {result}")
    case "*":
        result = num1 * num2
        print(f"The result is {result}")
    case "/":
        if num2 == 0:
            print("Error: Cannot divide by zero!")
        else:
            result = num1 / num2
            print(f"The result is {result}")
    case _:
        print("Invalid operation. Please choose +, -, *, or /.")
