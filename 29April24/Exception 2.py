try:
    x = int(input("enter a number"))
    result=10/x
except ZeroDivisionError as error:
    print("error",error)
except ValueError as error:
    print("error",error)
finally:
    print("i will print how ever")