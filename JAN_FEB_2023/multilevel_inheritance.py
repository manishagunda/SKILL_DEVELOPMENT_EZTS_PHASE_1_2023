#multilevel inheritance
class manisha:
    car=500000
    def get(self):
        print(self.car)
        
        
class son(manisha):
    bike=200000
    def put(self):
        print(self.bike)

class grandson(son):
    bankaccount=32210000
    def display(self):
        print(self.bankaccount)
s=grandson()
s.put()
s.get()
s.display()
