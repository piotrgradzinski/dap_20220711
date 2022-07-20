"""
Write a program that will calculate the result of the given operation
(adding, subtracting, multiplying, dividing) based on the two numbers given.
If an incorrect operation is specified, the program should display an appropriate error message.

Sample program output:
Enter the first number: 10
Enter the second number: 5
Enter the type of operation (+, -, *, /): +
Result: 10 + 5 = 15
"""

while True:
    user_input = input('Enter the first number or end to stop: ')
    if user_input == 'end':
        break

    number_1 = float(user_input)
    number_2 = float(input('Enter the second number: '))
    operation = input('Enter the type of operation (+, -, *, /): ')

    if operation == '+':
        result = number_1 + number_2
    elif operation == '-':
        result = number_1 - number_2
    elif operation == '*':
        result = number_1 * number_2
    elif operation == '/':
        result = number_1 / number_2
    else:
        result = None

    if result is None:
        print('You have provided wrong operation!')
    else:
        print(f'{number_1} {operation} {number_2} = {result}')
