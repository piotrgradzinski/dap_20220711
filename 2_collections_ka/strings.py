# str
# Strings are ordered and not mutable. Every element of a string is a string with length = 1

string = "asdf"

# print(f"{len(string)}")
print(f"{len(string) = }")

print(f"{string[1] = }")
print(f"{type(string[1]) = }")

for character in string:
    print(character)

# `in` operator - checks for existence of an element within collection
numbers = [10, 20, 30, 40]
print(f"{10 in numbers = }")
print(f"{15 in numbers = }")
print(f"{1020 in numbers = }")

# `in` operator for strings - checks for the existence of a whole substring
string = "Mary had a little lamb"
print(f'{"a" in string = }')
print(f'{"lit" in string = }')
print(f'{"til" in string = }')

characters = list(string)
print(f"{characters = }")
print(f'{"lit" in characters = }')

word = "adam"
print(word.upper())
print(word.capitalize())
print(word.split("a"))