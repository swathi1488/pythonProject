file=open("test_data",'r')
print(file.read())

print("********************")

file=open("test_data","r")
print(file.readline())

print("&&&&&&&&&&&&&&&&&&&&")

line=open("test_data",'r')
print(line.readlines())
for i in line:
    print(i,end='')
