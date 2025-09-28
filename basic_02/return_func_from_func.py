def fun1(name):
    def fun2():
        return "Hello, " + name + "!"
    return fun2 # returning the nested function as reference
greet_func = fun1("shakshi") # assigning the returned function to a variable
print(greet_func())  # Output: Hello, shakshi!

# return function without arguments
def fun3():
    def fun4():
        return "Hello, World!"
    return fun4 # returning the nested function as reference
greet_func2 = fun3() # assigning the returned function to a variable
print(greet_func2())  # Output: Hello, World!

# return function with arguments
def fun5(name):
    def fun6(greeting):
        return f"{greeting}, {name}!"
    return fun6 # returning the nested function as reference
greet_func3 = fun5("Ankit") # assigning the returned function to a variable
print(greet_func3("Hi"))  # Output: Hi, Ankit!

print(greet_func3("Hello"))  # Output: Hello, Ankit!

# return function with multiple arguments
def fun7(x, y):
    def fun8():
        return x + y
    return fun8 # returning the nested function as reference
sum_func = fun7(10, 20) # assigning the returned function to a variable
print(sum_func())  # Output: 30
print(sum_func())  # Output: 30
print(sum_func())  # Output: 30
print(sum_func())  # Output: 30

