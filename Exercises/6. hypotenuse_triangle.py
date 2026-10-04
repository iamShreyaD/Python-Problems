import math

a = float(input("Enter the first side of the triangle: "))
b = float(input("Enter the second side of the triangle: "))

c = round(math.sqrt((a ** 2) + (b ** 2)), 2)

print(f"The hypotenuse of the triangle is {c} cm.")
