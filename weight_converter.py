weight = float(input("Enter weight: "))
unit = input("Kilograms or Pounds? (K or L): ").lower()

if unit == "k":
    weight = weight * 2.205
    unit = "Lbs."
elif unit == "l":
    weight = weight / 2.205
    unit = "Kgs."
else:
    print(f"{unit} was not valid.")

print(f"The weight is: {round(weight, 1)} {unit}")