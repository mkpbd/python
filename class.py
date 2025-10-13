

# Class & Object
# A class is an user-defined prototype for an object that defines a set of attributes that characterize any object of the class. 
# The attributes are data members (class variables and instance variables) and methods, accessed via dot notation.

# An object refers to an instance of a certain class. 
# For example, an object named obj that belongs to a class Circle is an instance of that class.
#  A unique instance of a data structure that is defined by its class. 
# An object comprises both data members (class variables and instance variables) and methods.


#define a class 

class Smartphone :
     # constructor    
   def __init__(self, device, brand):
      self.device = device
      self.brand = brand
   
   # method of the class
   def description(self):
      return f"{self.device} of {self.brand} supports Android 14"

# creating object of the class
phoneObj = Smartphone("Smartphone", "Samsung")
print(phoneObj.description()) 


# ===================== Encapsulation ===============================================
# Data members of class are available for processing to functions defined within the class only.
# Functions of class on the other hand are accessible from outside class context.
# So object data is hidden from environment that is external to class. 
# Class function (also called method) encapsulates object data so that unwarranted access to it is prevented.

class Desktop:
   def __init__(self):
      self.__max_price = 25000  # is private  property or variables 

   def sell(self):
      return f"Selling Price: {self.__max_price}"

   def set_max_price(self, price):
      if price > self.__max_price:
         self.__max_price = price

# Object
desktopObj = Desktop()
print(desktopObj.sell()) 

# modifying the price directly
desktopObj.__max_price = 35000
print(desktopObj.sell()) 

# modifying the price using setter function
desktopObj.set_max_price(35000)
print(desktopObj.sell())        


#================== Inheritance ====================


# define parent class
class Parent:        
   parentAttr = 100
   def __init__(self):
      print ("Calling parent constructor")

   def parentMethod(self):
      print ("Calling parent method")

   def setAttr(self, attr):
      Parent.parentAttr = attr

   def getAttr(self):
      print ("Parent attribute :", Parent.parentAttr)

# define child class
class Child(Parent):   # inheritance form parent Class 
   def __init__(self):
      print ("Calling child constructor")

   def childMethod(self):
      print ("Calling child method")

# instance of child
c = Child()  
# child calls its method        
c.childMethod() 
# calls parent's method     
c.parentMethod()  
# again call parent's method   
c.setAttr(200)  
# again call parent's method     
c.getAttr()          


