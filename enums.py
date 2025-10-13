# importing enum 
from enum import Enum

class subjects2(Enum):
   ENGLISH = 1
   MATHS = 2
   SCIENCE = 3
   SANSKRIT = 4

obj = subjects2.MATHS
print (type(obj))


from enum import Enum, unique

@unique
class subjects1(Enum):
   ENGLISH = 1
   MATHS = 2
   GEOGRAPHY = 3
   SANSKRIT = 2



class subjects(Enum):
   ENGLISH = "E"
   MATHS = "M"
   GEOGRAPHY = "G"
   SANSKRIT = "S"
   
obj = subjects.SANSKRIT
print(type(obj))
print(obj.name)
print(obj.value)