"""
Write a program that counts occurrences of positive and negative numbers in a given list of integers.
"""

# https://en.wikipedia.org/wiki/Negative_number
# zero is usually (but not always) thought of as neither positive nor negative

numbers = [1, 2, 3, -100, -10, 0, 4]

positive_numbers = []
negative_numbers = []

for number in numbers:
    if number > 0:
        positive_numbers.append(number)
    elif number < 0:
        negative_numbers.append(number)

print(positive_numbers)
print(negative_numbers)
print(f'Negatives: {len(negative_numbers)}, positives: {len(positive_numbers)}')
