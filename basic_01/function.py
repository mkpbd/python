def fun():
    return "Hello, World!"
print(fun())

def even_or_odd(num):
    if num % 2==0:
        return "Even"
    else:
        return "Odd"
    
even_or_odd(3)


def my_function(x, y=50):
    return x + y
print(my_function(5))

def student(firstname, lastname):
    print(firstname, lastname)

student("John", "Doe")

def nameAge(name, age):
    print(f"{name} is {age} years old." )

nameAge("Alice", 30)

def myfunc(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(f"{key}: {value}")

myfunc(1, 2, 3, name="Bob", age=25)


# function within functions 

def f1():
    def f2():
        return "Hello from f2"
    return f2()
f1()

#anonymous function

def cube(x): return x*x*x
print(cube(3))

#lambda function
square = lambda x: x * x
print(square(4))

def  pass_by_refernce(x):
    x[0] = 100
    print("Inside function:", x)

print(x = [1, 2, 3])

# recursion function 
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))


