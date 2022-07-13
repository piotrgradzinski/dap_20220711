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
