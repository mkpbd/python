"""Python set is an unordered collection of multiple items having different datatypes. In Python, sets are mutable, unindexed and do not contain duplicates. The order of elements in a set is not preserved and can change.

Can store None values.
Implemented using hash tables internally.
Do not implement interfaces like Serializable or Cloneable.
Python sets are not inherently thread-safe; synchronization is needed if used across threads."""

# Creating Sets
a = {1, 2, 3, 4, 5}               # Set of integers
b = {'a', 'b', 'c', 'd', 'e'}     # Set of strings
c = {1, 'a', 2.5, True, None}      # Set of mixed data types
d = {True, False, None}            # Set of boolean and None values
print(a)
print(b)
print(c)
print(d)
# Note: Sets are created using curly braces {} or the set() function.
# Note: Sets do not allow duplicate values. If we try to add a duplicate value, it will be ignored.
# Note: Sets are unordered, so the order of elements may not be the same as the order in which they were added.
# Note: Sets are mutable, so we can add or remove elements from a set.
# Note: We can create an empty set using the set() function. Using {} will create an empty dictionary.
e = set()  # Empty set
print(e)
print(type(e))  # <class 'set'>
# Note: We can create a set from a list, tuple, or string using the set() function.
f = set([1, 2, 3, 4, 5])    # Set from list
g = set(('a', 'b', 'c', 'd', 'e'))  # Set from tuple
h = set('hello')  # Set from string (duplicates will be removed)
print(f)
print(g)
print(h)
# Note: The set created from the string 'hello' will contain only unique characters: {'h', 'e', 'l', 'o'}
# Note: Sets can contain elements of different data types, including integers, strings, floats, booleans, and None.
# Note: Sets cannot contain mutable elements like lists or dictionaries, but they can contain immutable elements like tuples.
i = {1, (2, 3), 4.5, 'hello'}
print(i)
# Note: The set 'i' contains an integer, a tuple, a float, and a string.
# Note: We cannot create a set with mutable elements like lists or dictionaries.
#j = {1, [2, 3], 4.5, 'hello'}  # This will raise a TypeError  # Uncommenting this line will cause an error
#print(j)
# Note: The above line will raise a TypeError because lists are mutable and cannot be added to a set.
# Note: We can use the len() function to get the number of elements in a set.
print(len(a))  # Number of elements in set a
print(len(b))  # Number of elements in set b
print(len(c))  # Number of elements in set c
print(len(d))  # Number of elements in set d
print(len(e))  # Number of elements in empty set e
print(len(f))  # Number of elements in set f
print(len(g))  # Number of elements in set g
print(len(h))  # Number of elements in set h
print(len(i))  # Number of elements in set i
#print(len(j))  # Number of elements in set j (will raise an error if uncommented)
# Note: The len() function returns the number of unique elements in the set.

# Accessing Set Elements
# Note: Sets are unordered, so we cannot access elements using indexing or slicing like we do with lists or tuples.
# Note: We can iterate through the elements of a set using a for loop.

for element in a:
    print(element)

for element in b:
    print(element)

for element in c:
    print(element)



for element in d:
    print(element)

for element in e:
    print(element)  # This will not print anything as the set is empty

for element in f:
    print(element)



## Add Elements into Set
a.add(6)          # Add integer 6 to set a
b.add('f')       # Add string 'f' to set b
c.add(3.5)      # Add float 3.5 to set c
d.add(None)     # Add None to set d
e.add(1)        # Add integer 1 to empty set e
f.add(6)        # Add integer 6 to set f


## Remove Elements from Set
a.remove(1)     # Remove integer 1 from set a
b.remove('a')   # Remove string 'a' from set b
c.remove(2.5)   # Remove float 2.5 from set c
d.remove(True)  # Remove boolean True from set d
e.remove(1)     # Remove integer 1 from set e
f.remove(1)     # Remove integer 1 from set f

## Remove Elements using Pop
a.pop()         # Remove and return an arbitrary element from set a
b.pop()         # Remove and return an arbitrary element from set b
c.pop()         # Remove and return an arbitrary element from set c
d.pop()         # Remove and return an arbitrary element from set d
e.pop()         # Remove and return an arbitrary element from set e
f.pop()         # Remove and return an arbitrary element from set f
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
# Note: The pop() method removes and returns an arbitrary element from the set.
# If the set is empty, it raises a KeyError.
# Note: We can also use the discard() method to remove an element from a set.
a.discard(2)    # Discard integer 2 from set a
b.discard('b')  # Discard string 'b' from set b

## Clear all elements from Set
a.clear()  # Clear all elements from set a
b.clear()  # Clear all elements from set b


## Fronzen Set
# Note: A frozenset is an immutable version of a set. Once created, we cannot add or remove elements from a frozenset.
fs = frozenset([1, 2, 3, 4, 5])  # Create a frozenset from a list
print(fs)
print(type(fs))  # <class 'frozenset'>
# Note: We can create a frozenset from a list, tuple, or string using the frozenset() function.
fs2 = frozenset(('a', 'b', 'c', 'd', 'e'))  # Create a frozenset from a tuple
fs3 = frozenset('hello')  # Create a frozenset from a string (duplicates will be removed)
print(fs2)
print(fs3)
# Note: The frozenset created from the string 'hello' will contain only unique characters: frozenset({'h', 'e', 'l', 'o'})
# Note: We cannot add or remove elements from a frozenset. The following lines will raise an AttributeError if uncommented.
#fs.add(6)        # This will raise an AttributeError
#fs.remove(1)     # This will raise an AttributeError
#fs.pop()         # This will raise an AttributeError
#fs.clear()       # This will raise an AttributeError


