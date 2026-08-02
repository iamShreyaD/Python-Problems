
# types
name = "Shreya"
print(type(name))

age = 23 
print(type(age))
print("Your age is: " + str(age))

# Math
password = "123fesg3s"
# Use case check password quality
print(len(password))

if len(password) < 8 :
    print("your password is too short")
# len() counts spaces

text = """
Python is easy to learn.
Python is powerful.
Many people love python.
"""

# count returns how many times a word appears in the string
print(text.count("Python"))   # 2

# replace swaps part of the text with something new
# "2026/05/10" to replace "/" with "-"
price = "1234,56"
print(price.replace(",", "."))

price = "$1,299.99"
print(price.replace("$", "").replace(",", ""))
