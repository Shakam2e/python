class employee:
    empcount=0
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        employee.empcount += 1
        
    def displaycount(self):
        print("total employee %d" % employee.empcount)

    def displayemployee(self):
        print ("Name:",self.name,"salary:",self.salary)

#creating instances of a class(objects) using class name and passing arguments
emp1=employee("zero",2000)
emp2=employee("minni",5000)
#calling the objects after instance creation
emp1.displayemployee()
emp2.displayemployee()
print("total employee %d" % employee.empcount)

