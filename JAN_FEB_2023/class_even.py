class company:
    num=20
    def put(self):
        if(self.num%2==0):
            print("even")
        else:
            print("odd")
c=company()
c.put()

#
class company:
    num=20
    def put(self,a):
        if(a%2==0):
            print("even")
        else:
            print("odd")
c=company()
c.put(101)