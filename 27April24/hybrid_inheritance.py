class A:
    def method_a(self):
        return "method a"
class B(A):
    def method_b(self):
        return "method b"
class C(A):
    def method_c(self):
        return  "method c"
class D(B,C):
    def method_d(self):
        return "method d"
d=D()
print(d.method_b())
print(d.method_a())
print(d.method_c())
print(d.method_d())