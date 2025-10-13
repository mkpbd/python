# Creating Singleton Classes in Python
# We can create and implement singleton classes in Python using the following ways −

# using __init__
# using __new__


class Singleton:
  __uniqueInstance = None

  @staticmethod
  def createInstance():
    if Singleton.__uniqueInstance == None:
      Singleton()
    return Singleton.__uniqueInstance
    
  def __init__(self):
      if Singleton.__uniqueInstance != None:
          raise Exception("Object exist!")
      else:
          Singleton.__uniqueInstance = self
           
obj1 = Singleton.createInstance()
print(obj1)
obj2 = Singleton.createInstance()
print(obj2)


