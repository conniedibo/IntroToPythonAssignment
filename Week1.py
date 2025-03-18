#Ask user to input two numbers
num1 = int(input ("Please type in first number:"))
num2 = int(input ("Please type in second number:"))
#Ask user to input a mathematical operation
operation = input("Enter the operation (+, -, *, /): ")

# Perform the operation
if operation == "+":
    print(num1+num2)
elif operation == "-":
    print(num1-num2)
elif operation == "*":
    print(num1*num2)
    
elif operation == "/":
    if num2 != 0:
        print(num1/num2)
    else:
        print("Error: Division by zero is not allowed!")
else:
    print("Invalid operation. Please enter +, -, *, or /")