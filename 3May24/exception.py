#file1=open('swathi.txt','a')
#file1.write("i want job quckly")
#file1.close()

#file3=open("pradeep.txt","a")
#file3.write("yesyesyes")
#file3.close()

file3=open("pradeep.txt","w")
op=file3.write("yesyesyes")
file3.close()

try:
   file=open("pradeep10.txt","r")
   print(file.read())
   file.close()
except FileNotFoundError as e:
    print("FileNotFoundError",e)

#from dir import module as p1
from PyPackage import module as p
print(p.sum(1,2))
#print(p1.sum(1,2))

import math
print(math.pow(2,3))

from PyPackage import module1
module1.Greet("pramod")
person=module1.Person("amith")
person.intro()
