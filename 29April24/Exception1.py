a=int(input("enter a number"))
b=int(input("enter a number"))
try:
    c=a/b
    print(c)
except Exception as error:
    print("your divisible a value with zero please dont do it",error)
finally:
    print("i will execute how ever")