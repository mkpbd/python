# We use square brackets [] to create a list directly.

a = [1,2,3,4,5,6,7,8,9,10]
b = ['a','b','c','d','e','f','g','h','i','j']
c = [1,'a',2,'b',3,'c',4,'d',5,'e']
d=[True, False, True, False]

print(a)
print(b)
print(c)
print(d)

#2. Using list() Constructor
e = list((1,2,3,4,5,6,7,8,9,10))
f = list(('a','b','c','d','e','f','g','h','i','j'))
g = list((1,'a',2,'b',3,'c',4,'d',5,'e'))
h = list((True, False, True, False))
print(e)
print(f)
print(g)
print(h)
# Note: We have to use double round brackets (()) while using list() constructor.
# because the first round bracket is for the list() function and the second round bracket is for the tuple.
# A tuple is very similar to a list except that tuples are immutable (they cannot be changed).
# We will learn more about tuples in the next tutorial.

#3. Creating List with Repeated Elements
i = [0]*10
j = ['a']*10
k = [1,2,3]*3
l = [True, False]*5

print(i)
print(j)
print(k)
print(l)
# Note: This method is used to create a list with repeated elements.
# We can also use this method to create a list of a specific size with all elements initialized to the same value.

#Accessing List Elements
print(a[0])  # First element
print(b[1])  # Second element
print(c[2])  # Third element
print(d[3])  # Fourth element
print(a[-1]) # Last element
print(b[-2]) # Second last element
print(c[-3]) # Third last element
print(d[-4]) # Fourth last element
# Note: We can access list elements using their index.
# Indexing starts from 0. So, the first element is at index 0, the second element is at index 1, and so on.
# We can also use negative indexing to access elements from the end of the list.
# The last element is at index -1, the second last element is at index -2, and so on.
# We can also use slicing to access a range of elements in a list.
print(a[0:5])  # First five elements
print(b[1:6])  # Second to sixth elements
print(c[2:8])  # Third to eighth elements
print(d[3:])   # Fourth element to the end

# Note: Slicing returns a new list containing the specified range of elements.

# Adding Elements into List
a.append(11)  # Add 11 at the end of the list
b.append('k') # Add 'k' at the end of the list
c.append(6)   # Add 6 at the end of the list
d.append(True) # Add True at the end of the list

print(a)
print(b)
print(c)
print(d)

# Updating Elements into List
a[0] = 0    # Update first element to 0
b[1] = 'z'  # Update second element to 'z'
c[2] = 20   # Update third element to 20
d[3] = None # Update fourth element to None
print(a)
print(b)
print(c)
print(d)
# Note: We can update list elements by accessing them using their index and assigning a new value.
# Lists are mutable, so we can change their elements.

# Removing Elements from List
a.remove(5)    # Remove element 5 from the list
b.remove('d')  # Remove element 'd' from the list
c.remove(2)    # Remove element 2 from the list
d.remove(False) # Remove element False from the list
print(a)
print(b)
print(c)
print(d)
# Note: We can remove elements from a list using the remove() method.
# The remove() method removes the first occurrence of the specified value.
# If the specified value is not found, it raises a ValueError.
# We can also use the pop() method to remove an element at a specific index.

a.pop(0)  # Remove the first element
b.pop(1)  # Remove the second element
c.pop(2)  # Remove the third element
d.pop(3)  # Remove the fourth element
print(a)
print(b)
print(c)
print(d)
# Note: The pop() method removes the element at the specified index and returns it.
# If no index is specified, it removes and returns the last element of the list.
# If the specified index is out of range, it raises an IndexError.

# We can also use the del keyword to remove an element at a specific index or to delete the entire list.
del a[0]  # Remove the first element
del b[1]  # Remove the second element
del c[2]  # Remove the third element
del d[3]  # Remove the fourth element
print(a)
print(b)
print(c)
print(d)
# Note: The del keyword can also be used to delete the entire list.
del a
del b
del c
del d
# print(a) # This will raise a NameError because the list 'a' has been deleted.

# Iterating Over Lists
a = [1,2,3,4,5,6,7,8,9,10]
b = ['a','b','c','d','e','f','g','h','i','j']
c = [1,'a',2,'b',3,'c',4,'d',5,'e']
d = [True, False, True, False,'e']
e = [True, False, True, False]  

for item in a:
    print(item, end=' ')
print()

for item in b:
    print(item, end=' ')
print()
for item in c:
    print(item, end=' ')
print()
for item in d:
    print(item, end=' ')
print()
for item in e:
    print(item, end=' ')
print()
# Note: We can iterate over the elements of a list using a for loop.
# The loop variable (item in this case) takes the value of each element in the list
# in each iteration of the loop.
# We can also use the range() function to iterate over the indices of the list.

for i in range(len(a)):
    print(a[i], end=' ')
print()

for i in range(len(b)):
    print(b[i], end=' ')
print()
for i in range(len(c)):
    print(c[i], end=' ')
print()

#Nested Lists
nested_list = [[1,2,3], ['a','b','c'], [True, False, True]]
print(nested_list)
print(nested_list[0])  # First sub-list
print(nested_list[1])  # Second sub-list
print(nested_list[2])  # Third sub-list
print(nested_list[0][0])  # First element of the first sub-list
print(nested_list[1][1])  # Second element of the second sub-list
print(nested_list[2][2])  # Third element of the third sub-list


