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
name = input("Enter your name: ")
if name == "":
    name = "Anonymous"

# Get monthly income (as a float)
# Remember to convert the input to a float!
monthly_income = float(input("Enter your monthly income: "))
if monthly_income <= 0:
    print("Error: Monthly income must be greater than 0.")
    exit()

# Get expenses for at least 4 categories:
# - rent: Rent/Housing
# - utilities: Utilities (electric, water, internet)
# - food: Food/Groceries
# - transportation: Transportation (gas, public transit)

def expense_input(prompt):
    value = float(input(prompt))
    if value < 0:
        return 0
    return value

rent = expense_input("Enter your monthly rent/housing expense: ")
utilities = expense_input("Enter your monthly utilities expense: ")
food = expense_input("Enter your monthly food/groceries expense: ")
transportation = float(input("Enter your monthly transportation expense: "))


# =============================================================================
# TODO: Task 2 - Perform Calculations
# =============================================================================
# Calculate total expenses
total_expenses = rent + utilities + food + transportation

# Calculate remaining balance (income - expenses)
remaining_balance = monthly_income - total_expenses

# Calculate savings rate as a percentage
# Formula: (balance / income) * 100
savings_rate = (remaining_balance / monthly_income) * 100

# Determine financial status
# - If balance > 0: status = "in the green"
# - If balance < 0: status = "in the red"
# - If balance == 0: status = "breaking even"
if remaining_balance > 0:
    status = "in the green"
elif remaining_balance < 0:
    status = "in the red"
else:
    status = "breaking even"

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

print("=" * 44)
print("       MONTHLY BUDGET REPORT")
print("=" * 44)
print(f"Name: {name}")
print(f"Monthly Income: ${monthly_income:.2f}")
print()
print("EXPENSES:")
print(f"  - Rent/Housing:    ${rent:.2f}")
print(f"  - Utilities:       ${utilities:.2f}")
print(f"  - Food/Groceries:  ${food:.2f}")
print(f"  - Transportation:  ${transportation:.2f}")
print("-" * 44)
print(f"Total Expenses: ${total_expenses:.2f}")
print(f"Remaining Balance: ${remaining_balance:.2f}")
print(f"Savings Rate: {savings_rate:.1f}%")
print()
print(f"Financial Status: {status}")
print("=" * 44)
print("       EXPENSES AS PERCENTAGE OF MONTHLY INCOME")
print("=" * 44)
print(f"Rent/Housing:    {(rent/monthly_income)*100:.1f}% of income")
print(f"Utilities:       {(utilities/monthly_income)*100:.1f}% of income")
print(f"Food/Groceries:  {(food/monthly_income)*100:.1f}% of income")
print(f"Transportation:  {(transportation/monthly_income)*100:.1f}% of income")
print("=" * 44)


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
