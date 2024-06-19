number = int(input("enter a number\n"))
if number < 0:
    print("factorial not possible")
else:
    fact = 1
    for i in range(1, number + 1):
        fact = fact * i
print("fact is:",fact)
