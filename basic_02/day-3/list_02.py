#-------============ List  or Array -----=====================
# Can contain duplicate items
# Mutable: items can be modified, replaced, or removed
# Ordered: maintains the order in which items are added
# Index-based: items are accessed using their position (starting from 0)
# Can store mixed data types (integers, strings, booleans, even other lists)


########################Creating a List ######################
#Lists can be created in several ways, such as using square brackets, the list() constructor or by repeating elements.

#====================== 1. List create using [] brackets  ========================

list_integer = [3,4,5,66,777,888,1111]  # integer list
list_string = ['kamal', 'passa','somon', 'jamal', 'tomal', 'roble'] # string list 
list_are_misxed_types = [2, 'kamal', True, 33, 'jamal'] # mixed Type list 

# ===================== 2. Using list() Constructor ===================
# We can also create a list by passing an iterable (like a tuple, string or another list) to the list() function.

ls = list((2,3,4,5)) # list of integer using constructor of list 
ls_s = list(('jamal', 'tomal', 'romal'))

# print(ls)
# ===================== 3. Creating List with Repeated Elements =====================

# rpls = [5]*5

# print(rpls)

# ================== Accessing List Elements ==================================

# Elements in a list are accessed using indexing. Python indexes start at 0, so a[0] gives the first element. Negative indexes allow access from the end

# ============================= Accessing List Elements ======================
# Elements in a list are accessed using indexing. Python indexes start at 0, so a[0] gives the first element. Negative indexes allow access from the end

a = [10, 20, 30, 40, 50]
# print(a[0])    
# print(a[-1])
# print(a[1:4])   # elements from index 1 to 3

# =================== Adding Elements into List ===================

# We can add elements to a list using the following methods:

# append(): Adds an element at the end of the list.
# extend(): Adds multiple elements to the end of the list.
# insert(): Adds an element at a specific position.
# clear(): removes all items.


a.append(6666); ## add single element at the end of list 
a.extend([3,4,5]) ## add multiple  element or other list 
a.insert(1,2222) ## add element in any spasific position 
a.clear() ## remove all element form list 
print(a)