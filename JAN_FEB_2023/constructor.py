class student:
    rollnum=28
    name="manisha"
    def __init__(self):
        print("wish u all success")
    def put(self):
        print(self.rollnum,self.name)
s=student()
s.put()

#constructor priority
class student:
    rollnum=28
    name="manisha"
    def put(self):
        print(self.rollnum,self.name)
    def __init__(self):
        print("wish u all success")
s=student()
s.put()

#2 constructors
class student:
    rollnum=28
    name="manisha"
    def __init__(self):
        print("all the best")
    def put(self):
        print(self.rollnum,self.name)
    def __init__(self):
        print("wish u all success")
s=student()
s.put()

