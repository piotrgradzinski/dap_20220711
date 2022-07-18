# this is a comment, python will not read this line

# f(x) = x + 1
# f(1) -> 2

print("Hello World!")
print("Lorem ipsum")

# DATA TYPES
# str - string data type
# literal - a value you put into your code -> https://en.wikipedia.org/wiki/Literal_(computer_programming)
# we can define strings in " or '
print("John Doe")
print('Jane Doe')

print('Book "Moby dick" is great')
print("Book \"Moby dick\" is great")

# int - integer, unlimited precision
print(10)
print(-1)
print(-123)

# float
print(2.5)
print(-4.9)
print(2.0)

# 2 different type than 2.0

print(3E5)  # 3*10^5 - scientific notation

# bool - boolean type, https://en.wikipedia.org/wiki/Boolean_algebra
print(True)
print(False)

# None - in python we have None, not NULL
print(None)

print(type(10))
print(type(10.0))
print(type("10"))

# OPERATORS
print(10        +         3)  # 13
print(10 - 3)  # 7
print(10 * 3)  # 30
print(10 / 3)  # 3.333333
print(10 // 3)  # 3
print(10 ** 3)  # 10 ^ 3
print(10 % 3)  # 1

# the process of connecting strings together: concatenation
print("I see" + "the cat")
print("I see the cat")

print("Tom" * 10)
print('-' * 100)

# variables
number = 10  # create a variable named number and assign 10 to this variable
print(number)

number = 'John'
print(number)

# when we are naming a variable we can't put spaces into the name
# naming convention in python -> _ instead of space
# https://realpython.com/python-pep8/#naming-conventions
first_name = 'John'  # in other languages firstName, FirstName
print(number)

# another way of creating strings
print("""Tom
John
Mark
Anna
""")
print('''Tom
John
Mark
Anna
''')


# printing multiple things
print('John', 10, True)  # 3 separate arguments


# concatenating different types
# print('My age is ' + 10)  # this will not work because we try to concatenate string with integer - we can only concatenate strings
print('My age is' + str(10))  # integer to string conversion

print('Moby dick')


# since python 3.6 we can do string concatenation in even easier way...
# we can f-strings: https://realpython.com/python-f-strings/

rate = 10.456
last_name = 'Doe'

# when we want to use f-string, we have to put f before quotes
print(f'My last name is {last_name}')
#       My last name is Doe

# with f-string we can use format specifiers: https://docs.python.org/3.9/library/string.html#formatspec
print(f'My last name is {last_name} and my rate is |{rate:_^10.1f}|')
#       My last name is Doe and my rate is 10.456

# without f-string
print('My last name is ' + last_name + ' and my rate is ' + str(rate))

# data types conversion
print('-' * 30)
# print('-' * '*')

# input function returns a string, always
my_variable = "12.345"
print(float(my_variable) + 5)

shoe_number_str = "46"
shoe_number_int = int(shoe_number_str)

print(shoe_number_str)
print(type(shoe_number_str))

print(shoe_number_int)
print(type(shoe_number_int))

print('-' * 30)

# Comparison operators
print(1 == 1)  # Warining! We have two = signs! One equal sign is an assignment operator
print(1 != 1)
print(2 > 1)
print(2 < 3)
print(1 <= 1)
print(1 >= 1)

print('-' * 10)

# Logical operators
print(True and True)
print(False or True)
print(not False)

print('-' * 10)

# https://stackoverflow.com/questions/4806911/how-are-strings-compared
print('abc' < 'b')

