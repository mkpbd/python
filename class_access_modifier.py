#Public members − A class member is said to be public if it can be accessed from anywhere in the program.

#Protected members − They are accessible from within the class as well as by classes derived from that class.

#Private members − They can be accessed from within the class only.


class Employee:
   'Common base class for all employees'
   def __init__(self, name="Bhavana", age=24):
      self.name = name  # public 
      self.age = age # public 

e1 = Employee()
e2 = Employee("Bharat", 25)

print ("Name: {}".format(e1.name))
print ("age: {}".format(e1.age))
print ("Name: {}".format(e2.name))
print ("age: {}".format(e2.age))


#To indicate that an instance variable is private, prefix it with double underscore (such as "__age").
# To imply that a certain instance variable is protected, prefix it with single underscore (such as "_salary").

class Employee1:
   def __init__(self, name, age, salary):
      self.name = name # public variable
      self.__age = age # private variable
      self._salary = salary # protected variable
   def displayEmployee(self):
      print ("Name : ", self.name, ", age: ", self.__age, ", salary: ", self._salary)

e1=Employee1("Bhavana", 24, 10000)

print (e1.name)
print (e1._salary)
print (e1.__age)