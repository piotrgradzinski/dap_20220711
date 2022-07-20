"""
Write a program listing all numbers from 0 to 100 that are divisible by 3 or by 5.
Also write how many such numbers occurred in this interval.

Numbers divisible by 3 or 5:
0
3
5
...
96
99
100

In the range 0-100 there are 48 numbers divisible by 3 or 5
"""

how_many = 0
for i in range(0, 101):
    if i % 3 == 0 or i % 5 == 0:
        print(i)
        how_many += 1

print()
print(how_many)

