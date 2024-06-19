# greater than,less than,equal using ternary operator
num1 = int(input("enter a number\n"))
num2 = int(input("enter a number\n"))
result = "greater" if num1>num2 else "less than" if  num1 < num2 else "equal to"
print(f"{num1} is {result} {num2}")