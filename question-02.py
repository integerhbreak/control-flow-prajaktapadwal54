num1 = int(input("Enter first number: "))  
num2 = int(input("Enter second number: ")) 
operation = input("Enter operation (+, -, *, /): ") 

if operation == '+':
    print("Result:", num1 + num2)
elif operation == '-':
    print("Result:", num1 - num2)
elif operation == '*':
    print("Result:", num1 * num2)
elif operation == '/' and num2 != 0:
    print("Result:", num1 / num2)
else:
    print("Invalid Operation or Division by Zero")
