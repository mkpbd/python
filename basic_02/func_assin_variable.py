# defining a function and assigning it to a variable
def greet(name):
    return f"Hello, {name}!"

# assigning the function to a variable
say_hello = greet
# calling the function using the new variable
print(say_hello("Alice"))  # Output: Hello, Alice!

# defining another function
def add(x, y):
    return x + y
# assigning the function to a variable
sum_function = add
# calling the function using the new variable
print(sum_function(5, 7))  # Output: 12

print(sum_function(10, 20))  # Output: 30
print(add(3, 4))  # Output: 7

