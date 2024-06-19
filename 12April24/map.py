numbers=[1,2,3,4,5]
def triple(a):
    return a*3
sq_list=list(map(triple,numbers))
print(sq_list)

sq_list2=list(map(lambda x:x*3 , numbers))
print(sq_list2)


list3=["dayam",True,2.3,67]
print(list3)