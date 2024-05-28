#access same property present in child,parent; access in child class
class college:
    def __init__(self,a):
        self.a=a
        print("hello buddy",self.a)
        
    def show(self):
        print("take care")

class ece(college):
    def __init__(self,a):
        super().__init__(a)
        
e=ece(100)
e.show()