# A tuple in Python is an immutable ordered collection of elements.

# Tuples are similar to lists, but unlike lists, they cannot be changed after their creation (i.e., they are immutable).
# Tuples can hold elements of different data types.
# The main characteristics of tuples are being ordered, heterogeneous and immutable.

# Creating Tuples
# 1. Using Parentheses ()
a = (1,2,3,4,5,6,7,8,9,10)
b = ('a','b','c','d','e','f','g','h','i','j')
c = (1,'a',2,'b',3,'c',4,'d', 5,'e')
d = (True, False, True, False)

# tuple with single element
e = (1,)          # Note the comma after 1
f = ('a',)       # Note the comma after 'a'
g = (True,)     # Note the comma after True
h = (3.14,)     # Note the comma after 3.14
print(a)
print(b)
print(c)
print(d)

## list using in tuple() 

list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = ['a','b','c','d','e','f','g','h','i','j']

tupleUsingList1 = tuple(list1) # Convert list1 to tuple
tupleUsingList2 = tuple(list2)  # Convert list2 to tuple
print(tupleUsingList1)
print(tupleUsingList2)  

## tuple basic operations

## accessing tuple elements
print(a[0])  # First element
print(b[1])  # Second element
print(c[2])  # Third element
print(d[3])  # Fourth element

print(a[-1]) # Last element
print(b[-2]) # Second last element
print(c[-3]) # Third last element
print(d[-4]) # Fourth last element

print(a[0:5])  # First five elements
print(b[1:6])  # Second to sixth elements   
print(c[2:8])  # Third to eighth elements
print(d[3:])   # Fourth element to the end

# Note: We can access tuple elements using their index.
# Indexing starts from 0. So, the first element is at index 0,
# the second element is at index 1, and so on.
# We can also use negative indexing to access elements from the end of the tuple.


## tuple concatenation
tuple1 = (1,2,3)
tuple2 = ('a','b','c')
tuple3 = tuple1 + tuple2
print(tuple3)  # Output: (1, 2, 3, 'a', 'b', 'c')
# Note: We can concatenate two or more tuples using the + operator.

## tuple repetition
tuple4 = (1,2,3)
tuple5 = tuple4 * 3
print(tuple5)  # Output: (1, 2, 3, 1, 2, 3, 1, 2, 3)

# Note: We can repeat a tuple multiple times using the * operator.
## tuple length
print(len(a))  # Output: 10
# Note: We can use the len() function to get the number of elements in a tuple.
## tuple membership
print(1 in a)      # Output: True
print('z' in b)    # Output: False
print(3 in c)      # Output: True
print(True in d)   # Output: True

## slicing tuple
print(a[2:5])  # Output: (3, 4, 5)
# Note: Slicing returns a new tuple containing the specified range of elements.
print(b[:4])   # Output: ('a', 'b', 'c', 'd')
print(c[::2])  # Output: (1, 2, 3, 4, 5)
print(d[::-1]) # Output: (False, True, False, True)
# Note: We can use slicing to access a range of elements in a tuple.
# The syntax for slicing is tuple[start:stop:step].

# Note: Since tuples are immutable, we cannot add, update or remove elements from a tuple after its creation.
# Any operation that tries to modify a tuple will raise a TypeError.
# For example, the following operations will raise errors if uncommented:
# a[0] = 100        # This will raise a TypeError
# b.append('k')    # This will raise an AttributeError

# del a[0]         # This will raise a TypeError
# a.remove(1)     # This will raise an AttributeError
# a.pop()         # This will raise an AttributeError

tup = tuple('GEEKSFORGEEKS')

# Removing First element
print(tup[1:])

# Reversing the Tuple
print(tup[::-1])

# Printing elements of a Range
print(tup[4:9])
# Note: We can delete the entire tuple using the del statement.

del tup
# print(tup)  # This will raise a NameError as tup is deleted
# Note: Tuples are immutable, so we cannot change their elements after creation.

# Note: Tuples can contain mutable elements like lists or dictionaries.
t = (1, 2, [3, 4], {'a': 5, 'b': 6})

print(t)

# We can modify the mutable elements inside the tuple
t[2][0] = 30  # Modifying the first element of the list inside the tuple
t[3]['a'] = 50  # Modifying the value of key 'a' in the dictionary inside the tuple
print(t)
# Note: The tuple 't' contains an integer, another integer, a list, and a dictionary.
# Note: We cannot change the elements of the tuple itself, but we can modify the mutable elements inside the tuple.






