class GrandFather:
    def grandfather_method(self):
        return "grandfather method"
class Father(GrandFather):
    def father_method(self):
        return "father method"
class son(Father):
    def son_method(self):
        return "son method"
child=son()
print(child.grandfather_method())
print(child.father_method())
print(child.son_method())