fruits = ["apple", "banana", "cherry" , "date"]
print(fruits)
print(fruits[0])          # first item
print(fruits[-1])         # last item
print(fruits[1:3])       # slice from index 1 to 2  
print(fruits[:3])        # slice from start to index 2
print(fruits[2:])        # slice from index 2 to end
print(fruits[-3:-1])     # slice from index -3 to -2
print(fruits[::2])       # slice with step 2
print(fruits[::-1])      # reverse the list
print(len(fruits))       # length of the list
fruits.append("elderberry")  # add item to the end
print(fruits)
fruits.insert(1, "blueberry") # insert item at index 1
print(fruits)
fruits.remove("banana")      # remove item by value
print(fruits)
popped_fruit = fruits.pop()  # remove and return last item
print("Popped fruit:", popped_fruit)
print(fruits)   
fruits.sort()    # sort the list
print(fruits)
fruits.sort(reverse=True)  # sort the list in descending order
print(fruits)
print(fruits.index("cherry"))  # index of item
print(fruits.count("apple"))    # count occurrences of item
fruits.extend(["fig", "grape"])  # extend list with another list
print(fruits)
fruits.clear()   # clear the list
print(fruits)
# Check if list is empty
print("Is the list empty?", len(fruits) == 0)
# Copy the list
fruits = ["apple", "banana", "cherry" , "date"]
fruits_copy = fruits.copy()
print("Copied list:", fruits_copy)
# Nested list
nested_list = [fruits, ["kiwi", "lemon"]]
print("Nested list:", nested_list)
print("First item of nested list:", nested_list[0][0])
# List comprehension
squared_numbers = [x**2 for x in range(10)]
print("Squared numbers:", squared_numbers)
# Flatten a nested list
flat_list = [item for sublist in nested_list for item in sublist]
print("Flattened list:", flat_list)
# Iterate through the list
for fruit in fruits:
    print("Fruit:", fruit)

# Enumerate through the list
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")
# Filter the list
filtered_fruits = [fruit for fruit in fruits if "a" in fruit]
print("Filtered fruits (contain 'a'):", filtered_fruits)
# Map the list to uppercase
upper_fruits = list(map(str.upper, fruits))
print("Uppercase fruits:", upper_fruits)