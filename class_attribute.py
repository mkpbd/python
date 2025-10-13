# Class Attributes (Variables)

class Employee:
   name = "Bhavesh Aggarwal"  # attribute or variables  name 
   age = "30" # attributes or variable  age 

# instance of the class
emp = Employee()
# accessing class attributes
print("Name of the Employee:", emp.name)
print("Age of the Employee:", emp.age)



# Modifying Class Attributes
class Employee1:
   # class attribute    
   empCount = 0
   def __init__(self, name, age):
      self.__name = name
      self.__age = age
      # modifying class attribute
      Employee.empCount += 1
      print ("Name:", self.__name, ", Age: ", self.__age)
      # accessing class attribute
      print ("Employee Count:", Employee.empCount)

e1 = Employee1("Bhavana", 24)
print()
e2 = Employee1("Rajesh", 26)