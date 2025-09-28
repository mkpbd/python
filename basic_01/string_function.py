# Step by step string functions in Python

# String functions
my_string = " Hello, welcome to the world of Python programming. "
print("Original String:", my_string)
# Length of the string
print("Length of the string:", len(my_string))
# Convert to uppercase
print("Uppercase:", my_string.upper())
#lowercase
print("Lowercase:", my_string.lower())
# Strip whitespace
print("Stripped String:", my_string.strip())
# Replace substring
print("Replace 'Python' with 'Java':", my_string.replace("Python", "Java"))
# Find substring
print("Find 'welcome':", my_string.find("welcome"))
# Split string
print("Split by space:", my_string.split(" "))
# Check if string starts with a substring
print("Starts with ' Hello':", my_string.startswith(" Hello"))
# Check if string ends with a substring
print("Ends with 'programming. ':", my_string.endswith("programming. "))
# Count occurrences of a substring
print("Count of 'o':", my_string.count("o"))
# Capitalize first letter
print("Capitalized String:", my_string.capitalize())
# Title case
print("Title Case String:", my_string.title())
# Check if all characters are alphabetic
print("Is alphabetic:", my_string.strip().isalpha())
# Check if all characters are numeric
print("Is numeric:", my_string.strip().isnumeric())
# Check if all characters are alphanumeric
print("Is alphanumeric:", my_string.strip().isalnum())
# Reverse the string
print("Reversed String:", my_string[::-1])
# Check if string is empty
print("Is empty string:", my_string == "")
# Join a list of strings
string_list = ["Python", "is", "fun"]
print("Join list of strings:", " ".join(string_list))
# Format string
formatted_string = "This is a {} string with number {}".format("formatted", 42)
print("Formatted String:", formatted_string)
# f-string (Python 3.6+)
name = "Alice"
age = 30
f_string = f"{name} is {age} years old."
print("f-String:", f_string)
# Check if string is digit
print("Is digit:", my_string.strip().isdigit())
# Check if string is whitespace
print("Is whitespace:", my_string.isspace())
# Swap case
print("Swap case:", my_string.swapcase())
# Center the string
print("Centered String:", my_string.center(50, '*'))
# Justify the string to the left
print("Left Justified String:", my_string.ljust(50, '-'))
# Justify the string to the right
print("Right Justified String:", my_string.rjust(50, '-'))
# Encode the string
print("Encoded String:", my_string.encode())
# Decode the string (example with utf-8)
encoded_string = my_string.encode()
print("Decoded String:", encoded_string.decode('utf-8'))
# Check if string is printable
print("Is printable:", my_string.isprintable())
# Expand tabs (example with tab characters)
tab_string = "Hello\tWorld"
print("Expand tabs:", tab_string.expandtabs(4))
# Partition the string
print("Partition 'welcome':", my_string.partition("welcome"))

s = "  \t Hello \n "
print(repr(s.strip()))   # removes both leading and trailing whitespace
print(repr(s.lstrip()))  # left only
print(repr(s.rstrip()))  # right only

s2 = "xxxhelloxxx"
print(s2.strip("x"))     # remove 'x' from both ends

csv = "apple,banana,cherry"
fruits = csv.split(",")      # => list
print(fruits)
print(" & ".join(fruits))    # join list back to string

text = "one two  three"
print(text.split())          # default splits on whitespace (multiple spaces collapsed)

txt = "apples apples apples"
print(txt.count("apples"))   # how many occurrences
print(txt.find("apples"))    # index of first, -1 if not found
print(txt.rfind("apples"))   # index of last
# difference: index() raises ValueError if not found
print(txt.startswith("app"))
print(txt.endswith("s"))
print("apple" in txt)        # membership test (True/False)

print("abc".isalpha())     # True: only letters
print("123".isdigit())     # True: only digits
print("a1".isalnum())      # True: letters+digits
print("   ".isspace())     # True: space-only string
print("This Is Title".istitle())  # True if each word is Titlecased
print("this is lower".islower())  # True if all cased chars are lowercase
print("THIS IS UPPER".isupper())  # True if all cased chars are uppercase       

print("This is a sentence.".endswith("."))  # True if ends with "."
print("This is a sentence.".capitalize())    # Capitalize first letter
print("this is a sentence.".title())          # Titlecase each word
print("swapCASE".swapcase())                  # swap case
print(" centered ".center(20, "-"))          # center in field of width 20, pad with '-'
print("left".ljust(10, "."))                 # left-justify in field of width 10, pad with '.'
print("right".rjust(10, "."))                # right-justify in field of width 10, pad with '.'
print("This is a sentence.".replace("sentence", "line"))  # replace substring
print("This is a sentence.".replace("is", "was", 1))      # replace first occurrence only
print("Hello\nWorld".expandtabs(4))          # expand tabs to spaces
print("Hello\nWorld".encode())                # encode to bytes
print(b'Hello World'.decode('utf-8'))        # decode back to string
print("Hello\nWorld".isprintable())          # False if contains \n or other non-printable chars
print("Hello\tWorld".expandtabs(4))          # expand tabs to spaces
print("Hello World".partition("lo"))         # split into 3-part tuple around substring
print("Hello World".rpartition("o"))        # split into 3-part tuple around last occurrence
print("  Hello  ".strip())                    # remove leading/trailing whitespace
print("xxxHelloxxx".strip("x"))               # remove 'x' from both ends
print("Hello World".zfill(20))                # pad with leading zeros to width 20
print("42".zfill(5))                          # pad with leading zeros to width 5
print("7.25".zfill(5))                        # pad with leading zeros to width 5


