# Data structures - collections

# Tuple
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

