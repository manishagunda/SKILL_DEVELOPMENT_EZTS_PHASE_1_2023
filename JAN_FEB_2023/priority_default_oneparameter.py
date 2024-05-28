#first argument constructor is more prior than default
class student:
    def __init__(self):
        print("take care")
    def __init__(self,a):
        self.a=a
        print("how are you",self.a)
    def show(self):
        print("wish u all success")
s=student(100)
s.show()
s1=student(100)