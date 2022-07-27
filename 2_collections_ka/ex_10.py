# Write a program that counts the number of occurrences of each
# character in the string given by the user
#
# Example:
# "aaababc"
# 'a': 4
# 'b': 2
# 'c': 1

freq = {}

text = input("Text:")
# with open("pi.txt", encoding="utf-8") as file:
#     text = file.read()

# for character in text:
#     if character in freq:
#         freq[character] += 1
#     else:  # else will be executed if this is the first time we find this character
#         freq[character] = 1

for character in text:
    if character not in freq:
        freq[character] = 0
    freq[character] += 1

print(freq)

