"""
Write a program that calculates the cost of travel from city A to city B
based on the number of kilometers given by the user, the price of fuel
and fuel consumption. Ask the user for the cities names.

Use a proportion formula to calculate this:
cost = distance * fuel_consumption / 100.0 * price

Sample program output:
City A: Warsaw
City B: Gdańsk
Distance Warsaw-Gdansk: 420
Fuel price: 4.55
Fuel consumption per 100 km: 5.5
The cost of the Warsaw-Gdańsk journey is 105 PLN
"""

city_a = input('City A: ')
city_b = input('City B: ')
distance = float(input(f'Distance between {city_a}-{city_b}: '))
price = float(input('Fuel price: '))
fuel_consumption = float(input('Fuel consumption: '))

cost = distance * fuel_consumption / 100.0 * price

print(f'The cost of the {city_a}-{city_b} journey is {cost} PLN.')
