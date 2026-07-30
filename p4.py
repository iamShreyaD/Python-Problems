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
