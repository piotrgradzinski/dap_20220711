# Write a program that counts the number of characters between the
# brackets <> in the string given by the user. Assume there is only
# one pair of brackets.
#
# Example:
# Mary had a <little> lamb
# 6

text = input("Enter text:")

are_we_inside_brackets = False
count = 0

for letter in text:
    if letter == "<":
        are_we_inside_brackets = True
    elif letter == '>':
        are_we_inside_brackets = False
    elif are_we_inside_brackets:
        count += 1

print(f"There are {count} characters between <> brackets.")

opening_idx = text.index("<")
closing_idx = text.index(">")

print(opening_idx, closing_idx)
print(closing_idx - opening_idx - 1)