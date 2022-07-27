empty = {}

price = {"bread": 3, "carrot": 1.5}

print(price)
print(f'{price["bread"] = }')
# print(f'{price["water"] = }') #  KeyError: no key "water" in the dictionary

# adding new key-value pair
price["water"] = 7  # this will add a new key "water"
print(f'{price["water"] = }')

# modifying values
price["water"] += 3  # this requires that "water" is already a key in the dictionary
print(f'{price["water"] = }')

price[10] = ["asdf", 103]
print(f"{price = }")

price[True] = "Truth is priceless"
print(f"{price = }")

# dictionary in for loop
for key in price:
    print(f"{key = }, value = {price[key]}")

for kv in price.items():
    # k, v = kv  # tuple assignment
    k = kv[0]
    v = kv[1]
    print(k, v)

print("-" * 30)

for k, v in price.items():
    print(k, v)


# check for key's existence
print(f"{'water' in price = }")
print(f"{'cheese' in price = }")