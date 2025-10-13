# parent class
class Universe: 
   def universeMethod(self):
      print ("I am in the Universe")

# child class
class Earth(Universe): 
   def earthMethod(self):
      print ("I am on Earth")
      
# another child class
class India(Earth): 
   def indianMethod(self):
      print ("I am in India")      

# creating instance 
person = India()  
# method calls
person.universeMethod() 
person.earthMethod() 
person.indianMethod() 

##===================== Hierarchical Inheritance
##============== This type of inheritance contains multiple derived 

# parent class
class Manager: 
   def managerMethod(self):
      print ("I am the Manager")

# child class
class Employee1(Manager): 
   def employee1Method(self):
      print ("I am Employee one")
      
# second child class
class Employee2(Manager): 
   def employee2Method(self):
      print ("I am Employee two")      

# creating instances 
emp1 = Employee1()  
emp2 = Employee2()
# method calls
emp1.managerMethod() 
emp1.employee1Method()
emp2.managerMethod() 
emp2.employee2Method()  



# parent class
class CEO: 
   def ceoMethod(self):
      print ("I am the CEO")
      
class Manager1(CEO): 
   def managerMethod(self):
      print ("I am the Manager")

class Employee11(Manager): 
   def employee1Method(self):
      print ("I am Employee one")
      
class Employee21(Manager, CEO): 
   def employee2Method(self):
      print ("I am Employee two")      

# creating instances 
emp = Employee21()
# method calls
emp.managerMethod() 
emp.ceoMethod()
emp.employee21Method()


## =================== The super() function
# In Python, super() function allows you to access methods and attributes of the parent class from within a child class.

# parent class
class ParentDemo:
   def __init__(self, msg):
      self.message = msg

   def showMessage(self):
      print(self.message)

# child class
class ChildDemo(ParentDemo):
   def __init__(self, msg):
      # use of super function
      super().__init__(msg)  

# creating instance
obj = ChildDemo("Welcome to Tutorialspoint!!")
obj.showMessage()  