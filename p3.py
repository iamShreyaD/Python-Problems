# int = 50, float = 3.14, str = "Hello", bool = True, list = [1, 2, 3], set = {1, 2}, tuple = (1, 2, 3, 4), dict = {'a':1, 'b':2, 'c':3}, NoneType = None


text = 'hi'
number = 10

print(type(text))
print(type(number))

print(len(text))
# print(len(number))

print(text.upper())
#bit_length() returns the length of a number in binary

print(number.bit_length())

# Create 5 variables - each with a different data type:
# 1. Your age
# 2. Your height (with decimals)
# 3. Your Name
# 4. Are you a student?
# 5. Something with no value yet
# Then print the values, data types, lengths of all variables.

age = input("Enter your age: ")
height = float(input("Enter your height in centimeters: "))
name = str(input("Enter your name: "))
status = bool(input("Are you a student?: "))
pet = input("Enter the name of your pet: ")

print(age)
print(height)
print(name)
print(status)
print(pet)

print(type(age))
