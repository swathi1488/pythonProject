my_dict={'a':1,'b':2,'c':3,'d':4}
value=my_dict.pop('b')
print(value)

value2=my_dict.items()
print(value2)
for i in my_dict.items():
    print(i)
print("***************")

value3=my_dict.popitem()
print(value3)
print(my_dict)