from abc import ABC, abstractmethod

# creating interface
class demoInterface(ABC):
   @abstractmethod
   def method1(self):
      print ("Abstract method1")
      return

   @abstractmethod
   def method2(self):
      print ("Abstract method1")
      return
   


# class implementing the above interface
class concreteclass(demoInterface):
   def method1(self):
      print ("This is method1")
      return
   
   def method2(self):
      print ("This is method2")
      return

# creating instance      
obj = concreteclass()

# method call
obj.method1()
obj.method2()