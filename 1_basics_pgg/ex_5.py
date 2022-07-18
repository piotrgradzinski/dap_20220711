"""
Write a program to check if the number given by the user:
is odd (number % 2 != 0), divisible by 3 (number % 3 == 0) and greater than 10 (number > 10)
or
is the number 7 (number == 7)
"""

number = int(input('Provide a number: '))

# https://docs.python.org/3/reference/expressions.html#operator-precedence
result = (number % 2 != 0 and number % 3 == 0 and number > 10) or number == 7

print(f'Result: {result}')
