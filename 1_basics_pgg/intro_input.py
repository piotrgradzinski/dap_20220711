# how we can get information from the user that is using our script?

# f(x) = x + 1
# f(1) -> 2

rate = input('Provide your hourly rate: ')
rate = float(rate)  # conversion to float data type

print(rate)
print(type(rate))

# I can do the same in 1 line
rate = float(input('Provide your hourly rate: '))
# rate = float("10.55")
# rate = 10.55

print(rate)
print(type(rate))


email = input('Provide your email address: ')
print(f'Your email is {email}')
