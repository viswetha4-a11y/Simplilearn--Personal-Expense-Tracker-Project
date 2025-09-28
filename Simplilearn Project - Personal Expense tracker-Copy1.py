#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# List to store all expenses
expenses = []

# Function to add an expense
def add_expense():
    try:
        date = input("Enter date (YYYY-MM-DD): ").strip()
        category = input("Enter category (e.g., Food, Travel): ").strip()
        amount = float(input("Enter amount spent: ").strip())
        description = input("Enter description: ").strip()
        
        # Check if any field is empty
        if not date or not category or not description:
            print("Error: All fields must be filled. Expense not added.")
            return
        
        expense = {
            'date': date,
            'category': category,
            'amount': amount,
            'description': description
        }
        expenses.append(expense)
        print("Expense added successfully!")
    
    except ValueError:
        print("Error: Amount must be a number. Expense not added.")

# Function to view all expenses
def view_expenses():
    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\nRecorded Expenses:")
    for i, exp in enumerate(expenses, start=1):
        # Validate the expense data
        if 'date' in exp and 'category' in exp and 'amount' in exp and 'description' in exp:
            print(f"{i}. Date: {exp['date']}, Category: {exp['category']}, Amount: ₹{exp['amount']:.2f}, Description: {exp['description']}")
        else:
            print(f"{i}. Incomplete expense entry found and skipped.")

# Example usage
while True:
    print("\nOptions:")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")
    
    choice = input("Choose an option (1-3): ").strip()
    
    if choice == '1':
        add_expense()
    elif choice == '2':
        view_expenses()
    elif choice == '3':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")


# In[ ]:


# List to store all expenses
expenses = []

# Variable to store monthly budget
monthly_budget = 0.0

# Function to add an expense
def add_expense():
    try:
        date = input("Enter date (YYYY-MM-DD): ").strip()
        category = input("Enter category (e.g., Food, Travel): ").strip()
        amount = float(input("Enter amount spent: ").strip())
        description = input("Enter description: ").strip()
        
        if not date or not category or not description:
            print("Error: All fields must be filled. Expense not added.")
            return
        
        expense = {
            'date': date,
            'category': category,
            'amount': amount,
            'description': description
        }
        expenses.append(expense)
        print("Expense added successfully!")
    
    except ValueError:
        print("Error: Amount must be a number. Expense not added.")

# Function to view all expenses
def view_expenses():
    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\nRecorded Expenses:")
    for i, exp in enumerate(expenses, start=1):
        if 'date' in exp and 'category' in exp and 'amount' in exp and 'description' in exp:
            print(f"{i}. Date: {exp['date']}, Category: {exp['category']}, Amount: ₹{exp['amount']:.2f}, Description: {exp['description']}")
        else:
            print(f"{i}. Incomplete expense entry found and skipped.")

# Function to set monthly budget
def set_budget():
    global monthly_budget
    try:
        budget = float(input("Enter your total budget for the month: ").strip())
        if budget <= 0:
            print("Budget must be greater than zero.")
            return
        monthly_budget = budget
        print(f"Monthly budget set to ₹{monthly_budget:.2f}")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Function to calculate total expenses and compare with budget
def track_budget():
    if monthly_budget == 0:
        print("Please set your monthly budget first.")
        return
    
    total_expenses = sum(exp['amount'] for exp in expenses if 'amount' in exp)
    print(f"\nTotal expenses so far: ₹{total_expenses:.2f}")
    
    if total_expenses > monthly_budget:
        print("Warning: You have exceeded your budget!")
    else:
        remaining = monthly_budget - total_expenses
        print(f"You have ₹{remaining:.2f} left for the month.")

# Main program loop
while True:
    print("\nOptions:")
    print("1. Set Monthly Budget")
    print("2. Add Expense")
    print("3. View Expenses")
    print("4. Track Budget")
    print("5. Exit")
    
    choice = input("Choose an option (1-5): ").strip()
    
    if choice == '1':
        set_budget()
    elif choice == '2':
        add_expense()
    elif choice == '3':
        view_expenses()
    elif choice == '4':
        track_budget()
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")


# In[ ]:


import csv
import os

# List to store all expenses
expenses = []

# Variable to store monthly budget
monthly_budget = 0.0

# CSV file to save/load expenses
filename = "expenses.csv"

# Function to add an expense
def add_expense():
    try:
        date = input("Enter date (YYYY-MM-DD): ").strip()
        category = input("Enter category (e.g., Food, Travel): ").strip()
        amount = float(input("Enter amount spent: ").strip())
        description = input("Enter description: ").strip()
        
        if not date or not category or not description:
            print("Error: All fields must be filled. Expense not added.")
            return
        
        expense = {
            'date': date,
            'category': category,
            'amount': amount,
            'description': description
        }
        expenses.append(expense)
        print("Expense added successfully!")
    
    except ValueError:
        print("Error: Amount must be a number. Expense not added.")

# Function to view all expenses
def view_expenses():
    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\nRecorded Expenses:")
    for i, exp in enumerate(expenses, start=1):
        if 'date' in exp and 'category' in exp and 'amount' in exp and 'description' in exp:
            print(f"{i}. Date: {exp['date']}, Category: {exp['category']}, Amount: ₹{exp['amount']:.2f}, Description: {exp['description']}")
        else:
            print(f"{i}. Incomplete expense entry found and skipped.")

# Function to set monthly budget
def set_budget():
    global monthly_budget
    try:
        budget = float(input("Enter your total budget for the month: ").strip())
        if budget <= 0:
            print("Budget must be greater than zero.")
            return
        monthly_budget = budget
        print(f"Monthly budget set to ₹{monthly_budget:.2f}")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Function to calculate total expenses and compare with budget
def track_budget():
    if monthly_budget == 0:
        print("Please set your monthly budget first.")
        return
    
    total_expenses = sum(exp['amount'] for exp in expenses if 'amount' in exp)
    print(f"\nTotal expenses so far: ₹{total_expenses:.2f}")
    
    if total_expenses > monthly_budget:
        print("Warning: You have exceeded your budget!")
    else:
        remaining = monthly_budget - total_expenses
        print(f"You have ₹{remaining:.2f} left for the month.")

# Function to save expenses to CSV
def save_expenses():
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['date', 'category', 'amount', 'description'])
        writer.writeheader()
        for exp in expenses:
            writer.writerow(exp)
    print(f"Expenses saved to {filename} successfully!")

# Function to load expenses from CSV
def load_expenses():
    global expenses
    if not os.path.exists(filename):
        return  # No file exists yet

    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        expenses = []
        for row in reader:
            try:
                # Convert amount back to float
                row['amount'] = float(row['amount'])
                expenses.append(row)
            except ValueError:
                print(f"Skipping invalid row: {row}")
    if expenses:
        print(f"Loaded {len(expenses)} expenses from {filename}.")

# Load previous expenses when program starts
load_expenses()

# Main program loop
while True:
    print("\nOptions:")
    print("1. Set Monthly Budget")
    print("2. Add Expense")
    print("3. View Expenses")
    print("4. Track Budget")
    print("5. Save Expenses")
    print("6. Exit")
    
    choice = input("Choose an option (1-6): ").strip()
    
    if choice == '1':
        set_budget()
    elif choice == '2':
        add_expense()
    elif choice == '3':
        view_expenses()
    elif choice == '4':
        track_budget()
    elif choice == '5':
        save_expenses()
    elif choice == '6':
        save_expenses()
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")


# In[ ]:


import csv
import os

# List to store expenses
expenses = []

# Variable to store monthly budget
monthly_budget = 0.0

# CSV file to save/load expenses
filename = "expenses.csv"

# ----- Expense Functions -----
def add_expense():
    try:
        date = input("Enter date (YYYY-MM-DD): ").strip()
        category = input("Enter category (e.g., Food, Travel): ").strip()
        amount = float(input("Enter amount spent: ").strip())
        description = input("Enter description: ").strip()
        
        if not date or not category or not description:
            print("All fields are required. Expense not added.")
            return
        
        expense = {'date': date, 'category': category, 'amount': amount, 'description': description}
        expenses.append(expense)
        print("Expense added successfully!")
    
    except ValueError:
        print("Amount must be a number. Expense not added.")

def view_expenses():
    if not expenses:
        print("No expenses recorded yet.")
        return
    print("\nRecorded Expenses:")
    for i, exp in enumerate(expenses, start=1):
        print(f"{i}. Date: {exp['date']}, Category: {exp['category']}, Amount: ₹{exp['amount']:.2f}, Description: {exp['description']}")

# ----- Budget Functions -----
def set_budget():
    global monthly_budget
    try:
        budget = float(input("Enter your total budget for the month: ").strip())
        if budget <= 0:
            print("Budget must be greater than zero.")
            return
        monthly_budget = budget
        print(f"Monthly budget set to ₹{monthly_budget:.2f}")
    except ValueError:
        print("Invalid input. Please enter a number.")

def track_budget():
    if monthly_budget == 0:
        print("Please set your monthly budget first.")
        return
    total_expenses = sum(exp['amount'] for exp in expenses)
    print(f"Total expenses so far: ₹{total_expenses:.2f}")
    if total_expenses > monthly_budget:
        print("Warning: You have exceeded your budget!")
    else:
        print(f"You have ₹{monthly_budget - total_expenses:.2f} left for the month.")

# ----- Save/Load Functions -----
def save_expenses():
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['date', 'category', 'amount', 'description'])
        writer.writeheader()
        for exp in expenses:
            writer.writerow(exp)
    print(f"Expenses saved to {filename}.")

def load_expenses():
    global expenses
    if os.path.exists(filename):
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            expenses = []
            for row in reader:
                try:
                    row['amount'] = float(row['amount'])
                    expenses.append(row)
                except ValueError:
                    print(f"Skipping invalid row: {row}")
        if expenses:
            print(f"Loaded {len(expenses)} expenses from {filename}.")

# ----- Interactive Menu -----
def menu():
    load_expenses()
    while True:
        print("\n---- Expense Tracker Menu ----")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Track Budget")
        print("4. Save Expenses")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ").strip()
        
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            track_budget()
        elif choice == '4':
            save_expenses()
        elif choice == '5':
            save_expenses()
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 5.")

# Run the interactive menu
menu()


# In[ ]:


print (menu())


# In[ ]:


info (menu)


# In[ ]:




