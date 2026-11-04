# Expense Tracker System - By Sailaja
import os
class Expense:
    def __init__(self, item, amount, date):
        self.item = item
        self.amount = amount
        self.date = date
    def display(self):
        return f"{self.item} - Rs.{self.amount} | Date: {self.date}"
expenses = []
FILE_NAME = "expenses.txt"
def add_expense(item, amount, date):
    try:
        if item == "":
            print("Error: Invalid input")
            return False
        amount = int(amount)
        expenses.append(Expense(item, amount, date))
        save_to_file()
        print(f"Expense Added: {item} - Rs.{amount}")
        return True
    except ValueError:
        print("Error: Please enter valid number")
        return False
def view_expenses():
    if len(expenses) == 0:
        print("No expenses found.")
        return
    for i, exp in enumerate(expenses, start=1):
        print(f"{i}. {exp.display()}")
def delete_expense(item_name):
    for exp in expenses:
        if exp.item.lower() == item_name.lower():
            expenses.remove(exp)
            save_to_file()
            print(f"Deleted: {item_name}")
            return True
    print("Item not found")
    return False
def calculate_total():
    total = sum(exp.amount for exp in expenses)
    print(f"Total Expenses: Rs.{total}")
    return total
def save_to_file():
    with open(FILE_NAME, "w") as f:
        for exp in expenses:
            f.write(f"{exp.item},{exp.amount},{exp.date}\n")
def load_from_file():
    try:
        if not os.path.exists(FILE_NAME):
            return
        with open(FILE_NAME, "r") as f:
            for line in f:
                p = line.strip().split(",")
                if len(p) == 3:
                    expenses.append(Expense(p[0], int(p[1]), p[2]))
    except FileNotFoundError:
        print("File not found")
def main():
    load_from_file()
    print("Welcome to Expense Tracker - By Sailaja")
    while True:
        print("\n1. Add Expense\n2. View Expenses\n3. Delete Expense\n4. Calculate Total\n5. Exit")
        c = input("Enter choice (1-5): ")
        if c == "1":
            add_expense(input("Item: "), input("Amount: "), input("Date: "))
        elif c == "2":
            view_expenses()
        elif c == "3":
            delete_expense(input("Item to delete: "))
        elif c == "4":
            calculate_total()
        elif c == "5":
            break
        else:
            print("Invalid choice")
if __name__ == "__main__":
    main()