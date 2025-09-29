# Python dictionary is a data structure that stores the value in key: value pairs. Values in a dictionary can be of any data type and can be duplicated, whereas keys can't be repeated and must be immutable.

# Keys are case sensitive which means same name but different cases of Key will be treated distinctly.
# Keys must be immutable which means keys can be strings, numbers or tuples but not lists.
# Duplicate keys are not allowed and any duplicate key will overwrite the previous value.
# Internally uses hashing. Hence, operations like search, insert, delete can be performed in Constant Time.
# From Python 3.7 Version onward, Python dictionary are Ordered.


# Creating a Dictionary# 1. Using Curly Braces {}
d1  = {1: 'apple', 2: 'banana', 3: 'cherry'}
d2 = {'name': 'John', 'age': 25, 'city': 'New York'}
d3 = {1: 'apple', 'age': 25, 2: 'banana', 'city': 'New York'}
d4 = {1: 'apple', 2: 'banana', 3: 'cherry', 1: 'orange'}  # Duplicate key, last value will overwrite
print(d1)
print(d2)
print(d3)

print(d4)  # Output will be {1: 'orange', 2: 'banana', 3: 'cherry'}
# Note: We can create a dictionary using curly braces {} with key: value pairs separated by commas.
# Note: Keys must be unique and immutable (cannot be changed). Values can be of any data type and can be duplicated.
# Note: If we use duplicate keys, the last value will overwrite the previous value.     
# Note: We can create an empty dictionary using empty curly braces {} or the dict() function.
d5 = {}  # Empty dictionary
d6 = dict()  # Empty dictionary using dict() function
print(d5)
print(d6)
print(type(d5))  # <class 'dict'>
print(type(d6))  # <class 'dict'>


# 2. Using dict() Constructor
d7 = dict({1: 'apple', 2: 'banana', 3: 'cherry'})
d8 = dict(name='John', age=25, city='New York')
d9 = dict([(1, 'apple'), (2, 'banana'), (3, 'cherry')])
d10 = dict(((1, 'apple'), (2, 'banana'), (3, 'cherry')))  # Note the double round brackets
print(d7)

## Accessing Dictionary Elements
print(d1[1])  # Accessing value using key
print(d2['name'])  # Accessing value using key
print(d3[2])  # Accessing value using key
print(d4[1])  # Accessing value using key (will return 'orange' due to overwrite)

# Note: We can access dictionary elements using their keys.
# Note: If we try to access a key that does not exist, it will raise a KeyError.

# Adding or Modifying Dictionary Elements
d1[4] = 'orange'  # Adding a new key-value pair
d2['age'] = 26    # Modifying an existing key's value
print(d1)

#Adding and Updating Dictionary Items
d3.update({5: 'grape'})  # Adding a new key-value pair using update() method
d4.update({'city': 'Los Angeles'})  # Modifying an existing key's value
print(d3)
print(d4)

# Note: We can add a new key-value pair by assigning a value to a new key.
# Note: We can modify an existing key's value by assigning a new value to the existing key.
# Note: We can also use the update() method to add or modify key-value pairs in a dictionary.
# Note: If the key already exists, the update() method will modify its value. If the key does not exist, it will add a new key-value pair.
# Note: We can use the len() function to get the number of key-value pairs in a dictionary.
print(len(d1))  # Number of key-value pairs in d1

# Removing Dictionary Elements
del d1[2]  # Removing a key-value pair using del statement
d2.pop('city')  # Removing a key-value pair using pop() method
d3.popitem()  # Removing the last inserted key-value pair using popitem() method
print(d1)
print(d2)
print(d3)

#Iterating Through a Dictionary
for key in d4:
    print(key, d4[key])

for key, value in d4.items():
    print(key, value)
# Note: We can remove a key-value pair using the del statement or the pop() method.
# Note: The popitem() method removes and returns the last inserted key-value pair as a tuple.
# Note: We can iterate through the keys of a dictionary using a for loop.
# Note: We can also iterate through the key-value pairs of a dictionary using the items() method.

# Note: We can delete the entire dictionary using the del statement.
del d5

# print(d5)  # This will raise a NameError as d5 is deleted
# Note: We can use the clear() method to remove all key-value pairs from a dictionary, making it empty.
d6.clear()
print(d6)  # Output will be {}
print(len(d6))  # Output will be 0
# Note: The clear() method does not delete the dictionary itself, it only removes all key-value pairs from it.

# Note: Dictionaries are mutable, so we can change their elements after creation.
# Note: We can use the keys() method to get a view of all keys in the dictionary.
print(d4.keys())  # Output will be dict_keys([1, 3, 4, 'city'])
# Note: We can use the values() method to get a view of all values in the dictionary.
print(d4.values())  # Output will be dict_values(['orange', 'cherry', 'grape', 'Los Angeles'])
# Note: We can use the items() method to get a view of all key-value pairs in the dictionary.

print(d4.items())  # Output will be dict_items([(1, 'orange'), (3, 'cherry'), (4, 'grape'), ('city', 'Los Angeles')])
# Note: The views returned by keys(), values(), and items() methods are dynamic and reflect changes made to the dictionary.
# Note: We can use the get() method to access the value of a key. If
# the key does not exist, it returns None or a specified default value.
print(d4.get(1))  # Output will be 'orange'
print(d4.get('country', 'USA'))  # Output will be 'USA' as 'country' key does not exist
print(d4.get('country'))  # Output will be None as 'country' key does not exist
# Note: Using get() method is safer than using square brackets [] as it does not raise a KeyError if the key does not exist.
# Note: We can use the setdefault() method to get the value of a key. If the key does not exist, it adds the key with a specified default value.
print(d4.setdefault(3, 'default'))  # Output will be 'cherry' as key 3 exists
print(d4.setdefault('country', 'USA'))  # Output will be 'USA' as
print(d4)  # 'country': 'USA' key-value pair will be added to d4
# 'country' key does not exist
# Note: The setdefault() method is useful for initializing keys with default values if they do not exist in the dictionary.

# Note: We can use the in keyword to check if a key exists in the dictionary.
print(1 in d4)      # Output: True
print('z' in d4)    # Output: False
print(3 in d4)      # Output: True
print(True in d4)   # Output: False
# Note: The in keyword checks for the existence of a key in the dictionary and returns a boolean value.

# Note: We can use the copy() method to create a shallow copy of a dictionary.
d11 = d4.copy()
print(d11)  # Output will be a copy of d4
# Note: The copy() method creates a new dictionary with the same key-value pairs as the

# original dictionary. Changes made to the copy will not affect the original dictionary and vice versa.
# Note: We can use the fromkeys() method to create a new dictionary with specified keys and a default value.
keys = ['a', 'b', 'c']
d12 = dict.fromkeys(keys, 0)  # Creating a dictionary with keys 'a', 'b', 'c' and default value 0

print(d12)  # Output will be {'a': 0, 'b': 0, 'c': 0}
# Note: The fromkeys() method creates a new dictionary with the specified keys and assigns the same default value to all keys.
# Note: If we do not specify a default value, it will be None by default.
d13 = dict.fromkeys(keys)  # Creating a dictionary with keys 'a', '
print(d13)  # Output will be {'a': None, 'b': None, 'c': None}
# Note: The fromkeys() method is useful for initializing a dictionary with a set of keys and a common default value.

# Note: Dictionaries can contain elements of different data types, including integers, strings, floats, booleans, None, lists, tuples, and even other dictionaries.

d14 = {1: 'apple', 'b': 2.5, 3: True, 'd': None, 5: [1, 2, 3], 'f': (4, 5), 'g': {'h': 6}}
print(d14)
# Note: The dictionary 'd14' contains keys and values of different data types, including

# integers, strings, floats, booleans, None, lists, tuples, and another dictionary.

# Note: We cannot use mutable elements like lists or dictionaries as keys in a dictionary, but we can use immutable elements like tuples.
# d15 = {[1, 2]: 'apple', {3: 4}: 'banana'}  # This will raise a TypeError  # Uncommenting this line will cause an error

# print(d15)


# Note: The above line will raise a TypeError because lists and dictionaries are mutable and cannot be used as keys in a dictionary.
# Note: We can use tuples as keys in a dictionary since they are immutable.
d16 = {(1, 2): 'apple', (3, 4): 'banana'}
print(d16)

# Note: The dictionary 'd16' contains tuples as keys and strings as values.

# Note: We can use the len() function to get the number of key-value pairs in a dictionary.
print(len(d14))  # Number of key-value pairs in d14

print(len(d16))  # Number of key-value pairs in d16

# Note: The len() function returns the number of key-value pairs in the dictionary.

