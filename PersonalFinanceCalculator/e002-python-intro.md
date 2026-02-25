# e002: Exercise - Python Introduction

## Overview

| Attribute | Value |
|-----------|-------|
| **Mode** | Implementation (Code Lab) |
| **Duration** | 2-3 hours |
| **Prerequisites** | c014-c019 (Python basics), d003 (Python basics demo) |
| **Deliverable** | A Python script that processes user input and produces formatted output |

---

## Learning Objectives

By completing this exercise, you will:

- Create and run Python scripts
- Use variables and appropriate data types
- Get user input and display formatted output
- Perform calculations with operators
- Apply string formatting with f-strings

---

## The Scenario

You're building a **Personal Finance Calculator** that helps users understand their monthly budget. The program will collect income and expense information, perform calculations, and display a formatted summary.

---

## Setup

### Prerequisites

- Python 3.x installed
- A code editor (VS Code recommended)
- Terminal access

### Getting Started

1. Navigate to the `starter_code/` folder
2. Open `budget_calculator.py` in your editor
3. Follow the tasks below to complete the program

---

## Core Tasks

### Task 1: Collect User Information (30 min)

Complete the section marked `# TODO: Task 1` in the starter code.

1. **Get the user's name:**

   ```python
   name = input("Enter your name: ")
   ```

2. **Get monthly income:**
   - Prompt: "Enter your monthly income: $"
   - Store as a float (remember to convert!)

3. **Get expenses (at least 4 categories):**
   - Rent/Housing
   - Utilities
   - Food/Groceries
   - Transportation
   - Store each as a float

**Hint:** Use `float(input("prompt"))` to get numeric input.

---

### Task 2: Perform Calculations (30 min)

Complete the section marked `# TODO: Task 2`.

1. **Calculate total expenses:**

   ```python
   total_expenses = rent + utilities + food + transportation
   ```

2. **Calculate remaining balance:**

   ```python
   balance = income - total_expenses
   ```

3. **Calculate savings rate (as percentage):**

   ```python
   savings_rate = (balance / income) * 100
   ```

4. **Determine financial status:**
   - If balance > 0: status = "in the green"
   - If balance < 0: status = "in the red"
   - If balance == 0: status = "breaking even"

---

### Task 3: Display Results (45 min)

Complete the section marked `# TODO: Task 3`.

Create a formatted budget report using f-strings:

```
============================================
       MONTHLY BUDGET REPORT
============================================
Name: [name]
Monthly Income: $[income]

EXPENSES:
  - Rent/Housing:    $[rent]
  - Utilities:       $[utilities]
  - Food/Groceries:  $[food]
  - Transportation:  $[transportation]
--------------------------------------------
Total Expenses:      $[total_expenses]
Remaining Balance:   $[balance]
Savings Rate:        [savings_rate]%

Status: You are [status]!
============================================
```

**Requirements:**

- All dollar amounts should show 2 decimal places (e.g., `$1234.56`)
- Savings rate should show 1 decimal place (e.g., `15.5%`)
- Use string alignment for neat columns

**Hint:** Use f-string formatting like `f"${amount:.2f}"` for currency.

---

### Task 4: Add Validation (30 min)

Enhance your program with basic validation:

1. **Name validation:**
   - If name is empty, use "Anonymous"

2. **Income validation:**
   - If income is negative or zero, print an error and exit

3. **Expense validation:**
   - If any expense is negative, treat it as 0

---

### Stretch Goal: Category Percentages (Optional, 30 min)

Add a section showing what percentage each expense is of total income:

```
EXPENSE BREAKDOWN:
  - Rent/Housing:    45.0% of income
  - Utilities:        8.3% of income
  - Food/Groceries:  16.7% of income
  - Transportation:  10.0% of income
```

---

## Expected Output Example

```
============================================
       MONTHLY BUDGET REPORT
============================================
Name: Alice
Monthly Income: $5000.00

EXPENSES:
  - Rent/Housing:    $1500.00
  - Utilities:       $150.00
  - Food/Groceries:  $400.00
  - Transportation:  $200.00
--------------------------------------------
Total Expenses:      $2250.00
Remaining Balance:   $2750.00
Savings Rate:        55.0%

Status: You are in the green!
============================================
```

---

## Definition of Done

- [ ] Program runs without errors
- [ ] Collects user name and at least 4 expense categories
- [ ] Correctly calculates total expenses, balance, and savings rate
- [ ] Displays formatted output with proper alignment
- [ ] Shows dollar amounts with 2 decimal places
- [ ] (Stretch) Shows category percentages

---

## Submission

1. Complete the `budget_calculator.py` script
2. Run the program with sample data
3. Take a screenshot of the output
4. Submit both the code file and screenshot

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| ValueError on input | Make sure to wrap numeric input with `int()` or `float()` |
| TypeError in calculation | Check that all values are numbers, not strings |
| Alignment issues | Use f-string width specifiers like `{value:>10}` |
