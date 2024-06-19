od={}
od['a']=20
od['d']=30
od['c']=50
od['b']=100
print(od)


keys=od. keys()
print(list(keys))
values=od.values()
print(list(values))
key_sorted=sorted(keys)
print(key_sorted)

value_sorted=sorted(values)
print(value_sorted)
od2={}
od2[key_sorted[0]]=90
od2[key_sorted[1]]=87
od2[key_sorted[2]]=49
od2[key_sorted[3]]=26
print(od2)
print(list(od2))
