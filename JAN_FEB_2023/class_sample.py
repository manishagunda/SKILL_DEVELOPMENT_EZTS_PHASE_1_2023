class company:
    rollnum=36
    name="manisha"
    salary=1000.55
    
    def display(self):
        print("rollnum:%d \nname:%s \nsalary:%f"%(self.rollnum,self.name,self.salary))
        
c=company()
c.display()