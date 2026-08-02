Challenge: Student Report Card Analyzer (Difficulty: 8/10)

A school wants a program that stores information about a student and analyzes the data types of the information entered.

Your program should ask the user for:

Student name
Age
Height (in centimeters)
Percentage in the last exam
Favorite subject
Whether the student plays sports (True or False)
Number of siblings

Store each value in a separate variable.

Part 1: Print the values

The output should look something like this:

Name: Shreya
Age: 23
Height: 165.5 cm
Percentage: 91.4
Favorite subject: Mathematics
Plays sports: True
Siblings: 1
Part 2: Print the data type of every variable

The output should look like this:

Type of name: <class 'str'>
Type of age: <class 'int'>
Type of height: <class 'float'>
Type of percentage: <class 'float'>
Type of plays_sports: <class 'bool'>

(Hint: use type().)

Part 3: Create new variables

Create these variables:

birth_year = 2026 - age

half_height = height / 2

percentage_in_decimal = percentage / 100

Print all three values.

Part 4: Prediction time 🧠

Without running the code, write down what you think the output type will be:

a = 10
b = 5.5
c = "20"
d = True

print(type(a + b))
print(type(c))
print(type(d))
print(type(a * 2))
print(type(b / 2))
Bonus challenge ⭐

Predict the output of these expressions:

print(bool(0))
print(bool(1))
print(bool(""))
print(bool("Python"))
print(bool(15))

Rules:

Use only input(), print(), variables, type(), and basic arithmetic.
No if statements.
No loops.
No functions.



# inputs for user
name = input("What is the name of the Student?: ")
age = int(input("What is the age of the student?: "))
height = round(float(input("What is the height of the student in centimeters?: ")), 1)
per = round(float(input("What is the percentage that the student secured in the last exam?: ")), 1)
subject = input("What is your favorite subject?: ")
is_sports = input("Does the student play any sport? Answer in yes or no: ").strip().lower() == 'yes'
no_sibs = int(input("How many siblings does the student have?: "))

# print answers
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height} cm")
print(f"Percentage is {per}%")
print(f"Favorite Subject: {subject}")
print(f"Plays sports: {is_sports}")
print(f"Siblings: {no_sibs}")

# data types
print(f"Type of name: {type(name)}")
print(f"Type of age: {type(age)}")
print(f"Type of heigh: {type(height)}")
print(f"Type of percentage: {type(per)}")
print(f"Type of plays_sports: {type(is_sports)}")

# creating variables
birth_year = 2026 - age
half_height = height / 2
percentage_in_decimal = per / 100

print(f"Birth year is {birth_year}")
print(f"Half height is {half_height}")
print(f"The percentage in decimal is {percentage_in_decimal}")

# a = 10
# b = 5.5
# c = "20"
# d = True

# print(type(a + b)) = float
# print(type(c)) = string
# print(type(d)) = bool
# print(type(a * 2)) = int
# print(type(b / 2)) = float

# Predict the output of these expressions:

# print(bool(0)) = False
# print(bool(1)) = True
# print(bool("")) = False
# print(bool("Python")) = True
# print(bool(15)) = True
