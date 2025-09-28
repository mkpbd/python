#user define function
def func(x):
    if(x % 2 == 0):
        return "even number"
    else:
        return "odd number"
print(func(10)) # function calling 

print(func(7)) # function calling

# function definition
def fun(name):
    print("Hello,", name)

# function call
fun("shakshi")

fun("Ankit")


# function definition
def fun1(name, age):
    print(name, "is", age, "years old.")

# function call
fun1(age=21, name="shakshi")
fun1(name="Ankit", age=22)


# function definition
def adds(*args):
    sum = 0
    for i in args:
        sum += i
    return sum
# function call
print(adds(1, 2, 3))

print(adds(10, 20, 30, 40, 50))

# function definition
def person(name, **kwargs):
    print("Name:", name)
    for key, value in kwargs.items():
        print(f"{key}: {value}")

person("shakshi", age=21, city="New York", profession="Engineer");
person("Ankit", age=22, city="Los Angeles", profession="Doctor");

# lambda function
square = lambda x: x * x
print(square(5))  # Output: 25

cube = lambda x: x * x * x
print(cube(3))    # Output: 27
add = lambda a, b: a + b
print(add(10, 20))  # Output: 30

multiply = lambda a, b: a * b
print(multiply(5, 4))  # Output: 20

# pass by reference
def modify_list(lst):
    lst.append(4)
    lst.append(5)
    lst.append(6)
    print("Inside function:", lst)
my_list = [1, 2, 3]
modify_list(my_list)
print("Outside function:", my_list)


# function definition
def fun_pass_reffernce(x):
    print("Value received:", x, "id:", id(x))

# driver code
x = 12
print("Value passed:", x, "id:", id(x))

# function call
fun_pass_reffernce(x)


# Function definition
def fun_ref(a):
    a[0] = 100  # Changing the first element of the list
    print("Inside function - lst:", a)

# Driver code
a = [1, 2, 3]  # List is mutable
print("Before function call - lst:", a)

# Function call
fun_ref(a)

print("After function call - lst:",a)  # List is modified outside the function