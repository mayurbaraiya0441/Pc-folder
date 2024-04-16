# Ex-6.1
# Create methods for the Calculator class that can do the following:

# Add two numbers.
# Subtract two numbers.
# Multiply two numbers.
# Divide two numbers
# example :
# 	calculator = Calculator()
# 	calculator.add(10, 5) ➞ 15
# 	calculator.subtract(10, 5) ➞ 5
# 	calculator.multiply(10, 5) ➞ 50
# 	calculator.divide(10, 5) ➞ 2



operator = input("Enter an operator (+ - * /): ")
num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))

if operator == "+":
    result = num1 + num2
    print(round(result, 3))
elif operator == "-":
    result = num1 - num2
    print(round(result, 3))
elif operator == "*":
    result = num1 * num2
    print(round(result, 3))
elif operator == "/":
    result = num1 / num2
    print(round(result, 3))
else:
    print(f"{operator} is not a valid operator")