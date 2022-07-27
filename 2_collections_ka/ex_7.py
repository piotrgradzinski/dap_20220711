string = input("Enter text:")

vowels = ('a', 'e', 'i', 'o', 'u')

count = 0

for letter in string:
    # if letter.lower() in "aeiou":
    if letter.lower() in vowels:
        count += 1

print(f'Number of vowels in text: {count}')
