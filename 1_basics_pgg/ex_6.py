"""
Write a program that will check the age of the person based on their year of birth.

Sample program output:
Enter year of birth: 1980
You are of legal age!
"""

year_of_birth = int(input('Enter year of birth: '))

age = 2022 - year_of_birth

if age >= 18:
    print('You are of legal age!')
else:
    print('You are not of legal age!')
