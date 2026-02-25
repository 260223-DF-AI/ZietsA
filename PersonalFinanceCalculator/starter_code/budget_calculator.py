# budget_calculator.py - Personal Finance Calculator
# Starter code for e002-exercise-python-intro

"""
Personal Finance Calculator
---------------------------
This program helps users understand their monthly budget by collecting
income and expense information and displaying a formatted summary.

Complete the TODO sections below to finish the program.
"""

print("=" * 44)
print("       PERSONAL FINANCE CALCULATOR")
print("=" * 44)
print()

# =============================================================================
# TODO: Task 1 - Collect User Information
# =============================================================================
# Get the user's name
# Example: name = input("Enter your name: ")
name = input("Enter name: ")
if (name == ""):
    name = "Anonymous"

# Get monthly income (as a float)
# Remember to convert the input to a float!
income = float(input("Enter monthly gross income: "))
while income < 0:
    print("ERROR")
    income = float(input("Enter monthly gross income: "))

# Get expenses for at least 4 categories:
# - rent: Rent/Housing
# - utilities: Utilities (electric, water, internet)
# - food: Food/Groceries
# - transportation: Transportation (gas, public transit)
rent = float(input("Enter rent: "))
if rent < 0:
    rent = 0
utilities = float(input("Enter utilities bill: "))
if utilities < 0:
    utilities = 0
food = float(input("Enter food bill: "))
if food < 0:
    food = 0
transportation = float(input("Enter transportation cost: "))
if transportation < 0:
    transportation = 0

print(f"       {name}: MONTHLY BUDGET")

# =============================================================================
# TODO: Task 2 - Perform Calculations
# =============================================================================
# Calculate total expenses
total_expense = rent + utilities + food + transportation
print(f"Total expense is {total_expense:.2f}")

# Calculate remaining balance (income - expenses)
balance = income - total_expense
print(f"Remaining balance is {balance:.2f}")

# Calculate savings rate as a percentage
# Formula: (balance / income) * 100
saving_rate = (balance/income)*100
print("Saving rate is ", saving_rate)

# Determine financial status
# - If balance > 0: status = "in the green"
# - If balance < 0: status = "in the red"
# - If balance == 0: status = "breaking even"

financial_status: str
if balance > 0:
    financial_status = "in the green"
elif balance < 0:
    financial_status = "in the red"
else:
    financial_status = "breaking even"

print("Financial Status: ", financial_status)


# =============================================================================
# TODO: Task 3 - Display Results
# =============================================================================
# Create a formatted budget report
# Use f-strings for formatting
# Dollar amounts should show 2 decimal places: f"${amount:.2f}"
# Percentages should show 1 decimal place: f"{rate:.1f}%"

# Example structure:
# print("=" * 44)
# print("       MONTHLY BUDGET REPORT")
# print("=" * 44)
# print(f"Name: {name}")
# ... continue building the report ...


# =============================================================================
# TODO: Task 4 - Add Validation (Optional Enhancement)
# =============================================================================
# Add these validations before calculations:
# - If name is empty, use "Anonymous"
# - If income is <= 0, print error and exit
# - If any expense is negative, treat as 0


# =============================================================================
# STRETCH GOAL: Category Percentages
# =============================================================================
# Add a section showing what percentage each expense is of total income
# Example: print(f"  - Rent/Housing:    {(rent/income)*100:.1f}% of income")
rent_expense = (rent/income)*100
print(f"Rent is {rent_expense:.2f} of income")
utilities_expense = (utilities/income)*100
print(f"Rent is {utilities_expense:.2f} of income")
food_expense = (food/income)*100
print(f"Rent is {food_expense:.2f} of income")
transportation_expense = (transportation/income)*100
print(f"Rent is {transportation_expense:.2f} of income")