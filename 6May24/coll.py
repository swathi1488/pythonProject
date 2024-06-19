from collections import Counter
cnt=Counter() #object created


list=["red","blue","white","blue","red"]
for word in list:
    cnt[word]=cnt[word]+1
print(cnt)
