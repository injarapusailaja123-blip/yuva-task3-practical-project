# Expense Tracker System - Task 3 Practical Implementation Project

**By:** Sailaja Injarapu
**Internship:** Yuva Internship - Python Development
**Task:** Task 3 - Practical Implementation Project
**GitHub:** https://github.com/injarapusailaja123-blip/yuva-task3-practical-project
**Technologies:** Python 3.10.11, VS Code, Git, GitHub, OOP, File Handling

---

## Project Overview

This is a real-world project built as part of Yuva Internship Task 3.
Expense Tracker System helps users to track their daily expenses easily.
User can add expense, view all expenses, delete expense, and calculate total expenses.

I applied all concepts learned in Task 1 and Task 2 - Python Fundamentals, OOP, File Handling, Error Handling, and Modular Design.

## Planning & Requirements

Before coding, I planned requirements clearly:

**User Requirements:**
1. User should be able to add expense with item name, amount, date
2. User should be able to view all expenses
3. User should be able to delete expense by name
4. User should be able to calculate total expenses
5. Data should be saved permanently even after closing program

**Breaking Down Complex Functionality:**
I broke the project into small components:
- Expense class - To store one expense
- add_expense() - To add new expense
- view_expenses() - To show all expenses
- delete_expense() - To delete expense
- calculate_total() - To calculate total
- save_to_file() / load_from_file() - To save data permanently

## Architecture & Design

**Architecture:** Python Core Only - No external libraries

**Data Storage:**
List of Objects. Example: {"item": "Food", "amount": 200, "date": "04-11-2026"}
File expenses.txt used as database

**Design Pattern:** Modular Design Pattern
Each function does only one work. Clean, readable and maintainable code.

**File Structure:**
yuva-task3-practical-project/
- src/main.py
- README.md
- requirements.txt
- .gitignore
- expenses.txt (auto-created)

## Implementation with Examples

**File:** src/main.py

**1. Add Expense Example:**
add_expense("Food", 200)
Output: Expense Added: Food - Rs.200

**2. View Expenses Example:**
view_expenses()
Output:
1. Food - Rs.200 | Date: 04-11-2026
2. Bus - Rs.50 | Date: 04-11-2026

**3. Calculate Total Example:**
calculate_total()
Output: Total Expenses: Rs.250

**4. Delete Expense Example:**
delete_expense("Food")
Output: Deleted: Food

I used if-else, loops, functions, OOP, try-except, docstrings and comments for clean code.

## How to Run

git clone https://github.com/injarapusailaja123-blip/yuva-task3-practical-project.git
cd yuva-task3-practical-project
python src/main.py

**Menu will appear:**
1. Add Expense
2. View Expenses
3. Delete Expense
4. Calculate Total
5. Exit

## Integration & Testing - Self-Assessment / Quiz Details

I tested the project with specific test cases:

Test 1: Add valid expense - add_expense("Books", 500) -> PASS, saved correctly.
Test 2: Empty input - add_expense("", 0) -> PASS Handled, Output: Error: Invalid input
Test 3: Wrong amount - add_expense("Food", "abc") -> PASS Handled by try-except, Output: Please enter valid number
Test 4: Delete non-existing item - delete_expense("Pizza") -> PASS, Output: Item not found
Test 5: File not found - Delete expenses.txt & Run -> PASS, Creates new file
Test 6: View empty list - view_expenses() with no data -> PASS, Output: No expenses found
Test 7: Total calculation - Food 200 + Bus 50 -> PASS, Total: Rs.250

These tests proved reliability and helped me identify knowledge gaps - like error handling for invalid input.

## Bug Fixing

Bug 1: File not found error when first time running
Fix: Used os.path.exists() check + try-except FileNotFoundError to create new file automatically.

Bug 2: Program crashed when user entered text instead of number for amount
Fix: Used try-except ValueError to show "Please enter valid number" instead of crashing.

## Documentation

Every function has docstring and comments. Architectural decisions documented in this README. Code is clean and maintainable for future developers.

## Learning Outcomes & Conclusion

I learned how to convert requirements into real code.
I gained confidence to build real projects independently.
I learned OOP, File Handling, and Error Handling practically.
This project is now a portfolio piece to showcase to employers.
Mentor feedback from Task 2 (56.8 marks) helped me add specific examples and detailed testing in this task.

## Author

Sailaja Injarapu - Yuva Intern - Python Development
