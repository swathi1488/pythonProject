#max of 3 numbers
num1=int(input("enter first number\n"))
num2=int(input("enter second number\n"))
num3=int(input("enter third number\n"))
max_value=num1 if (num1>num2 and num1>num3) else num2 if (num2>num3) else num3
print(f"maximum value {num1} {num2} and {num3} is: {max_value}")