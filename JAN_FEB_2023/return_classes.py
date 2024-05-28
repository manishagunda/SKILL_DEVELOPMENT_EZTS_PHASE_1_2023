class add:
    def sum(self,a,b):
        return a+b
class mul:
    def multi(self,a,b):
        return a*b
class calculator(add,mul):
    def divide(self,a,b):
        return a/b
d=calculator()
print(d.sum(100,200))
print(d.multi(100,200))
print(d.divide(100,200))

#
class add:
    def sum(self,a,b):
        print(a+b)
class mul:
    def multi(self,a,b):
        print(a*b)
class calculator(add,mul):
    def divide(self,a,b):
        print(a/b)
d=calculator()
(d.sum(100,200))
(d.multi(100,200))
(d.divide(100,200))