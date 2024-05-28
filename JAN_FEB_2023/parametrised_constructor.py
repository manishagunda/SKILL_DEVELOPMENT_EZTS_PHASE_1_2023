class student:
    def __init__(self,name,age,rollnum):
        print("this is parameterised constructor")
        self.name=name
        self.age=age
        self.rollnum=rollnum
    def show(self):
        print("wish u all success",self.name,self.age,self.rollnum)
s=student("manisha",19,36)
s.show()
