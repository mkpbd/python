# Creating Class Methods in Python

class Employee:
   empCount = 0  # attribute or variable 
   def __init__(self, name, age):
      self.__name = name
      self.__age = age
      Employee.empCount += 1
   def showcount(self):  # class method 
      print (self.empCount)
      
   counter = classmethod(showcount)

e1 = Employee("Bhavana", 24)
e2 = Employee("Rajesh", 26)
e3 = Employee("John", 27)

e1.showcount()
Employee.counter()


#==================== Using @classmethod Decorator ===================

class Employee1:
    empCount = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Employee.empCount += 1

    @classmethod
    def showcount(cls):
        print (cls.empCount)

    @classmethod
    def newemployee(cls, name, age):
        return cls(name, age)

e1 = Employee1("Bhavana", 24)
e2 = Employee1("Rajesh", 26)
e3 = Employee1("John", 27)
e4 = Employee1.newemployee("Anil", 21)

Employee1.showcount()