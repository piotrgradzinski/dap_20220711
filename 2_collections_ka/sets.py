# Sets are mutable and unordered.

# empty = {}  # this is a dictionary, not a set
empty = set()

numbers = {10, 3, 14, 12, 1, 2}

print(numbers)
print(type(numbers))
print({"one", "two", "three", "four", "five"})  # sets are unordered

numbers.add(20)
print(f"{numbers = }")
numbers.add(20)  # sets store only unique elements, so this line does nothing
print(f"{numbers = }")
print(f"{len(numbers) = }")

text = "Mary had a little lamb"
unique = set()
for character in text:
    unique.add(character)
print(unique)

print(f"{set(text) = }")

# set operators
A = {1, 2, 3}
B = {3, 4, 5}
print(f"{A = }")
print(f"{B = }")
print(f"{A | B = }")  # union - every element from both sets
print(f"{A - B = }")  # difference - every element from A that is not in B
print(f"{B - A = }")  # difference - every element from B that is not in A
print(f"{A & B = }")  # intersection - every element that is in both A and B
print(f"{A ^ B = }")  # symmetric difference - every element that appears in A or B but not in both
print(f"{(A - B) | (B - A) = }")