phone_book1=dict(rowdy=123456789,ganga=23456,putra=2345678)
print(phone_book1['rowdy'])
print(phone_book1["putra"])


new_dict=dict(name="swathi",age=26,is_famale=True,address="eluru")
print(new_dict["age"])
print(new_dict.get('age'))

new_dict1={"a":1,"b":2,"c":3,"a":95}
print(new_dict1)

keys=new_dict1.keys()
values=new_dict1.values()
print(keys)
print(values)

keys_list=list(keys)
print(keys_list[0])
print(keys_list[1])
print(keys_list[2])

print("***************")
values_list=list(values)
print(values_list[0])
print(values_list[1])
print(values_list[2])