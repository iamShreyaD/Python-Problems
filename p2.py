
# Challenge: Employee Salary Summary Generator

# A company wants a very simple Python program that records details of a new employee and prints a formatted salary report.

# The program should ask the user for:

# Employee Name
# Employee ID
# Department
# Age
# Monthly Basic Salary
# Monthly Bonus
# Tax Deduction
# Provident Fund Deduction
# Number of years worked
# Favorite Programming Language

# Store every value in its own variable.

# Now calculate

# Create variables for:

# Gross Salary
# Total Deductions
# Net Monthly Salary
# Annual Salary

# where

# Gross Salary = Basic Salary + Bonus

# Total Deductions = Tax + PF

# Net Salary = Gross Salary - Total Deductions

# Annual Salary = Net Salary × 12

# Remember that input() returns text, so you'll need to convert the salary values to numbers.

# Output Format

# Your program should print something like this (spacing doesn't have to match exactly):

# =========================================
#         EMPLOYEE INFORMATION
# =========================================

# Name               : Rahul Sharma
# Employee ID        : EMP104
# Department         : Data Analytics
# Age                : 24
# Experience         : 2 years
# Favorite Language  : Python

# -----------------------------------------
# Monthly Basic Salary : $5000.0
# Monthly Bonus       : $500.0
# Gross Salary        : $5500.0

# Tax Deduction       : $400.0
# PF Deduction        : $250.0
# Total Deductions    : $650.0

# Net Monthly Salary  : $4850.0
# Annual Salary       : $58200.0

# =========================================
# Thank you for using Employee Salary System
# =========================================


input_name = input("Enter your name:")
name = "Name: " + input_name

input_employeeID = input("Enter your employee ID:")
employee_ID = "Employee ID: " + input_employeeID

input_dept = input("Enter your department:")
dept = "Department: " + input_dept

input_age = input("Enter your age:")
age = "Age:" + input_age

input_m_basic_salary = int(input("Enter your monthly basic salary:"))
m_basic_salary = "Monthly Basic Salary: $" + input_m_basic_salary

input_m_bonus = int(input("Enter your monthly bonus: "))
m_bonus = "Montly Bonus: $" + input_m_bonus

my_gross_salary = input_m_basic_salary + input_m_bonus
gross_salary = "Gross Salary: $" + my_gross_salary

input_tax_ded = int(input("Enter your tax deductions: "))
tax_ded = "Tax Deductions: $" + input_tax_ded

input_pf_ded = int(input("Enter your provident fund deduction: "))
pf_ded = "PF Deductions: $" + input_pf_ded

input_total_ded = input_tax_ded + input_pf_ded
total_ded = "Total Deductions: $" + input_total_ded

input_net_salary = my_gross_salary - input_total_ded
net_salary = "Net Monthly Salary: $" + input_net_salary

input_annual_salary = input_net_salary * 12
annual_salary = "Annual Salary: $" + input_annual_salary

input_exp = input("Enter your total experience in years:")
exp = "Name:" + input_exp

input_fav_lan = input("Enter your favorite programming language:")
fav_lan = "Name:" + input_fav_lan

print("=========================================")
print("           EMPLOYEE INFORMATION")
print("=========================================")
print()
print(name)
print(employee_ID)
print(dept)
print(age)
print(exp)
print(fav_lan)
print()
print("-----------------------------------------")
print(m_basic_salary)
print(m_bonus)
print(gross_salary)
print()
print(tax_ded)
print(pf_ded)
print(total_ded)
print()
print(net_salary)
print(annual_salary)
print("=========================================")
print("Thank you for using employee salary system")
print("=========================================")
