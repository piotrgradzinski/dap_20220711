"""
Write a program that will display the results of multiplication of two numbers (1-10).
1*1=1
1*2=2
...
3*4=12
...
10*10=100
"""

for number_a in range(1, 11):
    for number_b in range(1, 11):
        print(f'{number_a} * {number_b} = {number_a * number_b}')
