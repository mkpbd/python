#print("hello Python");
from file import countNumber

print(countNumber([1,2,3,4,5,1,1,1], 1));


# string   '', double quotes "", triple quotes ''' ''', """ """
# list     [], list()
# tuple    (), tuple()
# dictionary   {}, dict()
# set      {}, set()
# boolean  True, False
# none     None
# integer  1, 2, 3
# float    1.1, 2.2, 3.3
# complex  1+2j, 2+3j
# operators  +, -, *, /, %, //, **, =, ==, !=, >, <, >=, <=, and, or, not, in, is
# conditional statements  if, elif, else
# loops  for, while, break, continue, pass  
# functions  def, return, lambda
# classes  class, self, __init__, inheritance
# exceptions  try, except, finally, raise, assert
# modules  import, from, as, dir(), help(), isinstance(), issubclass()
# file handling  open(), read(), write(), close(), with
# list comprehensions  [expression for item in iterable if condition]   
# dictionary comprehensions  {key: value for item in iterable if condition}
# set comprehensions  {expression for item in iterable if condition}
# generators  yield, next(), iter()
# decorators  @decorator, functools.wraps
# context managers  with, __enter__, __exit__
# type hints  def func(arg: type) -> return_type:
# f-strings  f"string {variable}"
# comments  # single line, ''' multi-line ''', """ multi-line """
# docstrings  """ Documentation """
# virtual environments  venv, pip, requirements.txt
# pip  install, uninstall, freeze, list, show, search
# common libraries  os, sys, math, random, datetime, re, json, requests, numpy, pandas, matplotlib, seaborn, sklearn, tensorflow, flask, django
# common functions  len(), range(), print(), input(), type(), str(), int(), float(), list(), dict(), set(), tuple(), sum(), min(), max(), sorted(), map(), filter(), zip(), enumerate()
# common methods  append(), extend(), insert(), remove(), pop(), clear(), index(), count(), sort(), reverse(), copy(), get(), keys(), values(), items(), update(), add(), discard(), union(), intersection(), difference()
# common attributes  __name__, __main__, __init__, __str__, __repr__, __dict__, __class__, __module__
# common exceptions  ValueError, TypeError, IndexError, KeyError, AttributeError, ImportError, ZeroDivisionError, FileNotFoundError, IOError, Exception
# common data structures  list, tuple, dictionary, set, string, integer, float, boolean, none
# common algorithms  sorting, searching, recursion, dynamic programming, greedy algorithms, divide and conquer, backtracking, graph algorithms, tree traversal
# common design patterns  singleton, factory, observer, decorator, strategy, adapter, facade, proxy, command, iterator, composite
# common testing frameworks  unittest, pytest, doctest, mock
# common debugging tools  pdb, logging, traceback, assert, print statements
# common version control systems  git, github, gitlab, bitbucket
# common IDEs  PyCharm, VSCode, Jupyter Notebook, Spyder, Anaconda
# common operating systems  Windows, macOS, Linux, Ubuntu, Fedora, CentOS
# common cloud platforms  AWS, Azure, Google Cloud, Heroku, DigitalOcean
# common databases  SQLite, MySQL, PostgreSQL, MongoDB, Redis
# common web frameworks  Flask, Django, FastAPI, Pyramid, Tornado
# common APIs  REST, GraphQL, SOAP
# common data formats  JSON, XML, CSV, YAML, Parquet

# common algorithms  sorting, searching, recursion, dynamic programming, greedy algorithms, divide and conquer, backtracking, graph algorithms, tree traversal
# common design patterns  singleton, factory, observer, decorator, strategy, adapter, facade, proxy, command, iterator, composite
# common testing frameworks  unittest, pytest, doctest, mock
# common debugging tools  pdb, logging, traceback, assert, print statements
# common version control systems  git, github, gitlab, bitbucket
# common IDEs  PyCharm, VSCode, Jupyter Notebook, Spyder, Anaconda
# common operating systems  Windows, macOS, Linux, Ubuntu, Fedora, CentOS   
# common cloud platforms  AWS, Azure, Google Cloud, Heroku, DigitalOcean
# common databases  SQLite, MySQL, PostgreSQL, MongoDB, Redis
# common web frameworks  Flask, Django, FastAPI, Pyramid, Tornado
# common APIs  REST, GraphQL, SOAP  
# common data formats  JSON, XML, CSV, YAML, Parquet
# common libraries  os, sys, math, random, datetime, re, json, requests, numpy, pandas, matplotlib, seaborn, sklearn, tensorflow, flask, django
# common functions  len(), range(), print(), input(), type(), str(), int(), float(), list(), dict(), set(), tuple(), sum(), min(), max(), sorted(), map(), filter(), zip(), enumerate()
# common methods  append(), extend(), insert(), remove(), pop(), clear(), index(), count(), sort(), reverse(), copy(), get(), keys(), values(), items(), update(), add(), discard(), union(), intersection(), difference()
# common attributes  __name__, __main__, __init__, __str__, __repr__, __dict__, __class__, __module__
# common exceptions  ValueError, TypeError, IndexError, KeyError, AttributeError, ImportError, ZeroDivisionError, FileNotFoundError, IOError, Exception
# common data structures  list, tuple, dictionary, set, string, integer, float, boolean, none
# common algorithms  sorting, searching, recursion, dynamic programming, greedy algorithms, divide and conquer, backtracking, graph algorithms, tree traversal
# common design patterns  singleton, factory, observer, decorator, strategy, adapter, facade, proxy, command, iterator, composite
# common testing frameworks  unittest, pytest, doctest, mock
# common debugging tools  pdb, logging, traceback, assert, print statements


#string
st1 = "hello python";
st2 = 'hello python';
st3 = '''hello python''';
st4 = """hello python""";

# numbers
num1 = 10;      # integer
num2 = 10.5;    # float
num3 = 1+2j;    # complex
num4 = 0b1010;  # binary
num5 = 0o12;    # octal
num6 = 0xA;     # hexadecimal
num7 = 10_000;  # underscore for readability
num8 = 1e3;     # scientific notation
num9 = 1.5e-2;  # scientific notation with negative exponent
num10 = float('inf');  # infinity
num11 = float('-inf'); # negative infinity
num12 = float('nan');  # not a number
num13 = complex(2, 3); # complex number using constructor
num14 = int(10.5);     # convert float to int
num15 = int('10');     # convert string to int
num16 = float('10.5'); # convert string to float
num17 = complex('2+3j'); # convert string to complex
num18 = round(10.567, 2); # round to 2 decimal places
num19 = abs(-10);      # absolute value
num20 = pow(2, 3);    # power
num21 = divmod(10, 3); # quotient and remainder
num22 = bin(10);      # binary representation
num23 = oct(10);      # octal representation
num24 = hex(10);      # hexadecimal representation
num25 = isinstance(num1, int); # check type
num26 = isinstance(num2, float); # check type
num27 = isinstance(num3, complex); # check type
num28 = isinstance(num4, int); # check type
num29 = isinstance(num5, int); # check type
num30 = isinstance(num6, int); # check type


#boolean
bool1 = True;
bool2 = False;
bool3 = (10 > 5);   # True
bool4 = (10 < 5);   # False
bool5 = (10 == 10); # True
bool6 = (10 != 5);  # True
bool7 = (10 >= 5);  # True
bool8 = (10 <= 5);  # False
bool9 = bool(1);    # True  
bool10 = bool(0);   # False
bool11 = bool([]);  # False
bool12 = bool([1,2,3]); # True
bool13 = bool('');  # False
bool14 = bool('hello'); # True
bool15 = not bool1; # False
bool16 = bool1 and bool2; # False  
bool17 = bool1 or bool2;  # True
bool18 = all([True, True, False]); # False
bool19 = any([True, False, False]); # True
bool20 = isinstance(bool1, bool); # True
bool21 = isinstance(bool2, bool); # True
bool22 = isinstance(bool3, bool); # True
bool23 = isinstance(bool4, bool); # True
bool24 = isinstance(bool5, bool); # True

# none
none1 = None;
none2 = type(None); # <class 'NoneType'>
none3 = (none1 is None); # True

# list
list1 = [1, 2, 3, 4, 5];
list2 = list((1, 2, 3, 4, 5));
list3 = ['a', 'b', 'c', 'd', 'e'];
list4 = [1, 'a', 2.5, True, None];
list5 = [];
list6 = [1, 2, 3] + [4, 5, 6]; # concatenation
list7 = [1, 2, 3] * 2; # repetition
list8 = list1[0]; # indexing
list9 = list1[-1]; # negative indexing  
list10 = list1[1:4]; # slicing
list11 = list1[:3]; # slicing
list12 = list1[2:]; # slicing   
list13 = list1[::-1]; # reversing
list14 = len(list1); # length
list15 = list1.append(6); # append
list16 = list1.extend([7, 8, 9]); # extend
list17 = list1.insert(0, 0); # insert   
list18 = list1.remove(3); # remove
list19 = list1.pop(); # pop
list20 = list1.pop(0); # pop with index
list21 = list1.clear(); # clear 
list22 = list1.index(4); # index
list23 = list1.count(1); # count
list24 = list1.sort(); # sort
list25 = list1.reverse(); # reverse
list26 = list1.copy(); # copy
list27 = list(range(1, 11)); # range
list28 = [x**2 for x in range(1, 11)]; # list comprehension
list29 = [x for x in list1 if x % 2 == 0]; # list comprehension with condition
list30 = isinstance(list1, list); # check type
list31 = isinstance(list2, list); # check type
list32 = isinstance(list3, list); # check type
list33 = isinstance(list4, list); # check type
list34 = isinstance(list5, list); # check type
list35 = isinstance(list6, list); # check type
list36 = isinstance(list7, list); # check type
list37 = isinstance(list8, int); # check type
list38 = isinstance(list9, int); # check type
list39 = isinstance(list10, list); # check type

# tuple
tuple1 = (1, 2, 3, 4, 5);
tuple2 = tuple((1, 2, 3, 4, 5));
tuple3 = ('a', 'b', 'c', 'd', 'e');
tuple4 = (1, 'a', 2.5, True, None);
tuple5 = ();
tuple6 = (1, 2, 3) + (4, 5, 6); # concatenation
tuple7 = (1, 2, 3) * 2; # repetition
tuple8 = tuple1[0]; # indexing
tuple9 = tuple1[-1]; # negative indexing
tuple10 = tuple1[1:4]; # slicing
tuple11 = tuple1[:3]; # slicing
tuple12 = tuple1[2:]; # slicing
tuple13 = tuple1[::-1]; # reversing
tuple14 = len(tuple1); # length
tuple15 = tuple1.count(1); # count
tuple16 = tuple1.index(4); # index
tuple17 = isinstance(tuple1, tuple); # check type
tuple18 = isinstance(tuple2, tuple); # check type
tuple19 = isinstance(tuple3, tuple); # check type
tuple20 = isinstance(tuple4, tuple); # check type

# dictionary
dict1 = {'a': 1, 'b': 2, 'c': 3};
dict2 = dict(a=1, b=2, c=3);
dict3 = {};
dict4 = dict1['a']; # indexing
dict5 = dict1.get('b'); # getting value
dict6 = dict1.keys(); # keys
dict7 = dict1.values(); # values
dict8 = dict1.items(); # items
dict9 = len(dict1); # length
dict10 = dict1.update({'d': 4}); # update
dict11 = dict1.pop('c'); # pop
dict12 = dict1.popitem(); # popitem
dict13 = dict1.clear(); # clear
dict14 = dict1.copy(); # copy
dict15 = isinstance(dict1, dict); # check type
dict16 = isinstance(dict2, dict); # check type
dict17 = isinstance(dict3, dict); # check type
dict18 = isinstance(dict4, int); # check type
dict19 = isinstance(dict5, int); # check type
dict20 = isinstance(dict6, dict_keys); # check type
dict21 = isinstance(dict7, dict_values); # check type
dict22 = isinstance(dict8, dict_items); # check type

# set
set1 = {1, 2, 3, 4, 5};
set2 = set((1, 2, 3, 4, 5));
set3 = set1.union({6, 7, 8}); # union
set4 = set1.intersection({3, 4, 5, 6, 7}); # intersection
set5 = set1.difference({4, 5, 6}); # difference
set6 = set1.symmetric_difference({4, 5, 6}); # symmetric difference
set7 = set1.add(6); # add
set8 = set1.remove(3); # remove
set9 = set1.discard(4); # discard
set10 = set1.pop(); # pop
set11 = set1.clear(); # clear
set12 = len(set1); # length
set13 = isinstance(set1, set); # check type
set14 = isinstance(set2, set); # check type
set15 = isinstance(set3, set); # check type
set16 = isinstance(set4, set); # check type
set17 = isinstance(set5, set); # check type
set18 = isinstance(set6, set); # check type
set19 = isinstance(set7, type(None)); # check type
set20 = isinstance(set8, type(None)); # check type
set21 = isinstance(set9, type(None)); # check type
set22 = isinstance(set10, int); # check type
set23 = isinstance(set11, type(None)); # check type
set24 = isinstance(set12, int); # check type
set25 = isinstance(set13, bool); # check type

# functions
def func1():
    return "Hello, World!"
def func2(x, y):
    return x + y
def func3(*args):
    return sum(args)
def func4(**kwargs):
    return kwargs
def func5(x=1, y=2):
    return x * y
def func6(x):
    return x**2
func7 = lambda x, y: x / y  # lambda function
def func8(x):
    """This is a docstring."""
    return x + 10   
def func9(x):
    pass  # empty function
def func10(x):
    if x < 0:
        raise ValueError("Negative value not allowed")
    return x
def func11(x):
    try:
        return 10 / x
    except ZeroDivisionError:
        return "Cannot divide by zero"
def func12(x):
    return isinstance(x, int)  # check type
def func13(x):
    return isinstance(x, float)  # check type

def func14(x):
    return isinstance(x, str)  # check type

# classes
class MyClass:
    class_var = "I am a class variable"
    
    def __init__(self, instance_var):
        self.instance_var = instance_var  # instance variable
    
    def instance_method(self):
        return f"Instance method called, instance_var: {self.instance_var}"
    
    @classmethod
    def class_method(cls):
        return f"Class method called, class_var: {cls.class_var}"
    
    @staticmethod
    def static_method():
        return "Static method called"
    
    def __str__(self):
        return f"MyClass with instance_var: {self.instance_var}"
    
    def __repr__(self):
        return f"MyClass(instance_var={self.instance_var})"
    
    def get_instance_var(self):
        return self.instance_var
    
    def set_instance_var(self, value):
        self.instance_var = value
