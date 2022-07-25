# Simple version
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# if i % 3 == 0 -> "Fizz"
# if i % 5 == 0 -> "Buzz"
# if i % 7 == 0 -> "Bzz"

print("-" * 40)

for i in range(1, 121):
    what_to_print = ""
    if i % 3 == 0:
        what_to_print += "Fizz" # the same as: what_to_print = what_to_print + "Fizz"
    if i % 5 == 0:
        # what_to_print += "Buzz"
        what_to_print = what_to_print + "Buzz"
    if i % 7 == 0:
        what_to_print += "Bzz"

    if what_to_print == "":  # we check if `what_to_print` is empty
        print(i)
    else:
        print(what_to_print)

