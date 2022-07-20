# Data structures - collections

# TUPLE
# (, )
# https://realpython.com/python-lists-tuples/
# - ordered
# - immutable - we can't change the content of the tuple after we created it

#    0   1   2
a = (10, 20, 30)
print(a)
print(type(a))

# access operator -> []
print( a[1] )
print( a[0] )

#    0   1     2        3     4
b = (10, 25.0, 'Piotr', True, None)
print(b)
print(b[3])

#    0       1                2
c = ((1, 2), ('a', 'b', 'c'), (True, False))
#     0  1    0    1    2      0     1

print(c)
print(c[1][2])

print('-' * 30)

# SLICING

#    0    1    2    3    4    5    6    7    8    9
d = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')
#    -10  -9   -8   -7   -6   -5   -4   -3   -2   -1

# d[start:stop:step]
print(d[0])  # a
print(d[1:3])  # left-closed, right-open, ('b', 'c')
print(d[1:5])  # ('b', 'c', 'd', 'e')
print(d[1:6])  # ('b', 'c', 'd', 'e', 'f')
print(d[1:10])  # ('b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')
print(d[:4])  # ('a', 'b', 'c', 'd') - we can skip start, it will mean to start from 0
print(d[4:])  # ('e', 'f', 'g', 'h', 'i', 'j') - we can skip end
print(d[:])  # we can even skip both :)
print(d[-1])  # j
print(d[-4:-2])  # ('g', 'h')
print(d[5:-2])  # ('f', 'g', 'h')
print(d[0:6:2])  # ('a', 'c', 'e')
print(d[::2])  # ('a', 'c', 'e', 'g', 'i')
print(d[::-1])  # ('j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a')


# useful methods

print(len(d))
print('c' in d)
print('q' not in d)

#    0   1   2   3   4
e = (10, 20, 30, 40, 50)
print(max(e))
print(min(e))
print(sum(e))

print(e.index(30))

f = (1, 2, 3)
g = (4, 5, 6)

h = f + g
print(h)

i = f * 3
print(i)

print('-' * 30)

# LIST
# [,]
# - mutable
# - ordered

#    0   1   2   3   4   5   6   7   8   9
a = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# access operator [] - it works exactly the same as for tuples
print(a[0])
print(a[::-1])

# we can change the content of the list
print(a)
a[0] = 11
print(a)

a.append(110)
print(a)

a.insert(1, 12)
print(a)

a.extend([200, 210, 220])
print(a)

a += [300, 310, 320]
print(a)

print(a)
a[1:3] = [1, 2]
print(a)

del(a[0])
print(a)

del(a[0:3])
print(a)

a.remove(310)
print(a)

a.sort()
print(a)

a.sort(reverse=True)
print(a)

# empty list creation
a = []
a = list()

print('-' * 30)

# how we can iterate through a list (or tuple)
# we can leverage for loop

list_of_numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for number in list_of_numbers:
    print(number)

print('---')

tuple_of_numbers = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
for number in tuple_of_numbers:
    print(number)

print('-' * 30)

# How I can iterate through a collection and have both index number and value?
list_of_numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for index, number in enumerate(list_of_numbers):
    print(f'{index} = {number}')

print('-' * 30)

# range function
# range(start, stop-1, step)
for i in range(11):
    print(i)

print('-' * 30)

for i in range(-5, 6):
    print(i)

print('-' * 30)

for i in range(-5, 6, 2):
    print(i)

print('-' * 30)


list_a = [1, 2, 3, 4, 5]
list_b = [10, 20, 30]

for number_a in list_a:
    for number_b in list_b:
        print(f'{number_a} + {number_b} = {number_a + number_b}')

print('-' * 30)

# We can treat strings as collection of characters
my_string = "To be or not be"

# access operator
print(my_string[0])
print(my_string[1:3])
print(my_string[::-1])

print(my_string.lower())
print(my_string.upper())
print(my_string.title())
print(my_string.capitalize())
print(my_string.casefold())
