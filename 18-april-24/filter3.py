products=[{"name":"laptop","price":1000},
          {"name":"smartphone","price":500},
          {"name":"tablet","price":300},{"name":"headphones","price":100}]
def is_afforadable(item):
    return item["price"]<500
afforadable_item=list(filter(is_afforadable,products))
print(afforadable_item)

print(afforadable_item[0]["name"]+str(afforadable_item[0]["price"]))
print(afforadable_item[1]["name"]+str(afforadable_item[1]["price"]))




def afforadable_item1(pramod):
    return len(pramod["name"])>6
afforadable_item_name=list(filter(afforadable_item1,products))
print(afforadable_item_name)
print(afforadable_item_name)

for i in afforadable_item_name:
    print(i["name"]+str(i["price"]))