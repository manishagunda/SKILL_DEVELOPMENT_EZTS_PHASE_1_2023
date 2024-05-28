#hierachial inheritance
class aaaa:
    jewels=100000
    def get(self):
        print(self.jewels)
class aaa1(aaaa):
    salary=250000
    def put(self):
        print(self.salary)
        print(self.jewels)
        self.get()
class aaa2(aaaa):
    home=900000
    def display(self):
        print(self.home)
class bbb1(aaaa):
    govtvalue=600000
    def access(self):
        print(self.govtvalue)
        
s1=aaa1()
s2=aaa2()
d1=bbb1()
s1.put()
s1.get()
s2.display()
s2.get()
d1.access()
d1.get()
