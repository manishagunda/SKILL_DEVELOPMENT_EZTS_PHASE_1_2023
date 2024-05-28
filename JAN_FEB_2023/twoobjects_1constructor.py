class student:
    def __init__(self,name,id):
        self.id=id
        self.name=name
    def display(self):
        print(self.id,self.name)
emp1=student("rahul",2000)
emp2=student("reddy",3000)
emp1.display()
emp2.display()
#two objects
class student:
    def __init__(self,name,id):
        self.id=id
        self.name=name
    def display(self):
        print(self.id,self.name)
emp1=student("rahul",2000)
emp2=student("reddy",3000)
emp2.display()
emp1.display()