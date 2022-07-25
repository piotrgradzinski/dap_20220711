weight = float(input("Provide your weight in kg: "))
height = float(input("Provide your height in cm: "))
height_in_meters_squared = (height / 100) ** 2
BMI = weight / height_in_meters_squared

if BMI <= 18.5:
    print(f"You are underweight")
# elif BMI > 18.5 and BMI <= 24.9:
# elif 18.5 < BMI <= 24.9:
elif BMI <= 24.9:
    print(f"You are of normal weight")
elif BMI <= 29.9:
    print(f"You are overweight")
else: # we already know that the BMI is > 29.9
    print(f"You have obesity")