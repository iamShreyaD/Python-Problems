# Python Calculator

operator = input("Enter an operator (+ - * /): ")


if operator not in ["+", "-", "*", "/"]:
    result = "Your input is invalid. Please choose an option from '+ - * /.'"
else:

    try:
        n1 = float(input("Enter the first number: "))
        n2 = float(input("Enter the second number: "))
        
        if operator == "+":
            result = round((n1 + n2), 9)
        elif operator == "-":
            result = round((n1 - n2), 9)
        elif operator == "*":
            result = round((n1 * n2), 9)
        elif operator == "/":
            if n2 == 0:
                result = "Oops! Division by zero is not allowed!"
            else:
                result = round((n1 / n2), 9)
        else:
            result = "Error! Please try again."

    except ValueError:
        result = "Enter a valid number."

print(result)
