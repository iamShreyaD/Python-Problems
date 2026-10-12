weight = float(input("Enter your weight: "))
unit = input("Kilograms or pounds (K/L): ")
unit = unit.lower()

if unit == "k":
    weight = round((weight * 2.205), 2)
    unit = "lbs"
    print(f"Your weight is {weight} {unit}.")

elif unit == "l":
    weight = round((weight / 2.205), 2)
    unit = "kgs"
    
else:
    print(f"The input of unit is invalid.")
