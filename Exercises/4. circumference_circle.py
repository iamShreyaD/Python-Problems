import math

radius = float(input("Enter the radius of circle: "))
circumference = 2 * math.pi * radius
c = str(round(circumference, 2))
print(f"The circumference of the circle is {c} cm.")
