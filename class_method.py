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
# Use of @classmethod() decorator is the prescribed way to define a class method as it is more convenient than first declaring an instance method and then transforming it into a class method.

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



#==================== Access Class Attributes in Class Method

class Cloth:
   # Class attribute
   price = 4000

   @classmethod
   def showPrice(cls):
      return cls.price

# Accessing class attribute
print(Cloth.showPrice())  

#=================== Dynamically Add Class Method to a Class =================

### The Python setattr() function is used to set an attribute dynamically.
#  If you want to add a class method to a class, pass the method name as a parameter value to setattr() function.


class Cloth1:
   pass

# class method
@classmethod
def brandName(cls):
   print("Name of the brand is Raymond")

# adding dynamically
setattr(Cloth1, "brand_name", brandName)
newObj = Cloth()
newObj.brand_name()

### ================= Dynamically Delete Class Methods

class Cloth2:
   # class method
   @classmethod
   def brandName(cls):
      print("Name of the brand is Raymond")

# deleting dynamically
del Cloth2.brandName
print("Method deleted")


##=============================== How to Create Static Method in Python? =====================

# There are two ways to create Python static methods −

# Using staticmethod() Function
# Using @staticmethod Decorator

class EmployeeStatic:
   empCount = 0
   def __init__(self, name, age):
      self.__name = name
      self.__age = age
      EmployeeStatic.empCount += 1
   
   # creating staticmethod
   def showcount():
      print (EmployeeStatic.empCount)
      return
   counter = staticmethod(showcount)



e1 = EmployeeStatic("Bhavana", 24)
e2 = EmployeeStatic("Rajesh", 26)
e3 = EmployeeStatic("John", 27)

e1.counter()

#================== Using @staticmethod Decorator ==============
class Student:
   stdCount = 0
   def __init__(self, name, age):
      self.__name = name
      self.__age = age
      Student.stdCount += 1
   
   # creating staticmethod
   @staticmethod
   def showcount():
      print (Student.stdCount)

e1 = Student("Bhavana", 24)
e2 = Student("Rajesh", 26)
e3 = Student("John", 27)

print("Number of Students:")
Student.showcount()