# 1.Creating a list
fruits = ["apple", "banana", "cherry"]
numbers = [10, 20, 30, 40]
mixed = [1, "hello", 3.5, True]

print(fruits)
print(numbers)
print(mixed)
# 2.Accessing elements
print(fruits[0])        # first item
print(fruits[-1])       # last item
print(fruits[1:3])      # slice from index 1 to 2
print(fruits[:2])       # slice from start to index 1

# 3.Modifying a list
fruits.append("date")          # add item to the end
print(fruits)
fruits.insert(1, "blueberry")  # insert item at index 1
print(fruits)
fruits.remove("banana")        # remove item by value
print(fruits)
popped_fruit = fruits.pop()    # remove and return last item
print("Popped fruit:", popped_fruit)
print(fruits)

 
# 4.List operations
fruits.sort()                  # sort the list
print(fruits)
fruits.sort(reverse=True)      # sort the list in descending order
print(fruits)
print(fruits.index("cherry"))  # index of item
print(fruits.count("apple"))   # count occurrences of item
fruits.extend(["fig", "grape"]) # extend list with another list
print(fruits)
fruits.clear()                 # clear the list
print(fruits)
# Check if list is empty
print("Is the list empty?", len(fruits) == 0)

# useful list methods
nums = [3, 1, 4, 1, 5, 9]

print(len(nums))     # length
print(min(nums))     # smallest
print(max(nums))     # largest
print(sum(nums))     # total sum

nums.sort()          # sort ascending
print(nums)

nums.sort(reverse=True) # sort descending
print(nums)

nums.reverse()       # reverse order
print(nums)

print(nums.count(1)) # count occurrences
print(nums.index(9)) # first index of value
nums.append(2)       # add to end
print(nums)
nums.insert(2, 6)    # insert at index

#List Comprehension
squared_numbers = [x**2 for x in range(10)]
print("Squared numbers:", squared_numbers)
# Flatten a nested list
nested_list = [[1, 2], [3, 4], [5]]
flat_list = [item for sublist in nested_list for item in sublist]
print("Flattened list:", flat_list)
# Iterate through the list

for fruit in ["apple", "banana", "cherry"]:
    print("Fruit:", fruit)
# Enumerate through the list
for index, fruit in enumerate(["apple", "banana", "cherry"]):
    print(f"Index {index}: {fruit}")
# Filter the list
filtered_fruits = [fruit for fruit in ["apple", "banana", "cherry"] if "a" in fruit]
print("Filtered fruits (contain 'a'):", filtered_fruits)
# Map the list to uppercase
upper_fruits = list(map(str.upper, ["apple", "banana", "cherry"]))
print("Uppercase fruits:", upper_fruits)
# Nested list
nested_list = [["apple", "banana"], ["cherry", "date"]]
print("Nested list:", nested_list)
print("First item of nested list:", nested_list[0][0])
# Copy the list
original = ["apple", "banana", "cherry"]
copy = original.copy()
print("Copied list:", copy)
# Merging lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged = list1 + list2
print("Merged list:", merged)
# Repeating lists
repeated = list1 * 3
print("Repeated list:", repeated)
# Check membership
print(2 in list1)  # True
print(5 not in list1)  # True
# Slicing with step
print(list1[::2])  # [1, 3]
print(list1[::-1]) # [3, 2, 1]
# Nested list comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print("Flattened matrix:", flattened)
# Iterate with index
for i in range(len(list1)):
    print(f"Index {i}, Value {list1[i]}")
# Using enumerate   
for i, val in enumerate(list1):
    print(f"Index {i}, Value {val}")
# List comprehension with condition
evens = [x for x in range(20) if x % 2 == 0]
print("Even numbers:", evens)
# Using map and filter
doubled = list(map(lambda x: x * 2, list1))
print("Doubled:", doubled)

