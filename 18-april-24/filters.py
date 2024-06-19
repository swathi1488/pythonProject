#filter-it filter the numbers less or equal from the list
numbers={1,2,3,4,5,6,7,8,9,10}
def is_even(num):
    return num%2==0
is_number=list(filter(is_even,numbers))
print(is_number)

#diffrence of map(it execute each and every number from list)
numbers1={1,2,3,4,5}
def square(x):
    return x**2
square_number=list(map(square,numbers1))
print(square_number)