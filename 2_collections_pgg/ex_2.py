"""
Write a program that calculates the average of numbers provided by the user.
To store the numbers use list. Allow up to 10 numbers to be entered. Use the `sum()` built-in function.
"""

numbers = []

while len(numbers) < 10:
    number = int(input('Provide a number: '))
    numbers.append(number)

average = sum(numbers) / len(numbers)

print(f'The average from the provided numbers equals {average:.2f}')
