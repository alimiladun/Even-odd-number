import csv
from datetime import datetime
import os

# Initialize the CSV file if it doesn't exist
def initialize_file():
    if not os.path.exists('transactions.csv'):
        with open('transactions.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Type', 'Category', 'Amount', 'Date'])

# Add a transaction (income/expense)
def add_transaction():
    transaction_type = input("Income or Expense? (I/E): ").upper()
    if transaction_type not in ['I', 'E']:
        print("Invalid type! Use 'I' for Income or 'E' for Expense.")
        return

    category = input("Category (e.g., Salary, Rent): ").strip()
    if not category:
        print("Category cannot be empty!")
        return

    try:
        amount = float(input("Amount: "))
        if amount <= 0:
            print("Amount must be positive!")
            return
    except ValueError:
        print("Invalid amount! Use numbers only.")
        return

    date_input = input("Date (YYYY-MM-DD, leave blank for today): ").strip()
    date = date_input if date_input else datetime.today().strftime('%Y-%m-%d')
    # Save to CSV
    with open('transactions.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([transaction_type, category, amount, date])
    print("Transaction added successfully!")

# View all transactions
def view_transactions():
    try:
        with open('transactions.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            print("\n--- Transactions ---")
            for idx, row in enumerate(reader, 1):
                type_label = "Income" if row[0] == 'I' else "Expense"
                print(f"{idx}. {type_label} | {row[1]} | ${float(row[2]):.2f} | {row[3]}")
    except FileNotFoundError:
        print("No transactions found!")

# Calculate remaining budget
def calculate_budget():
    total_income = 0
    total_expense = 0
    try:
        with open('transactions.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                amount = float(row[2])
                if row[0] == 'I':
                    total_income += amount
                else:
                    total_expense += amount
        remaining = total_income - total_expense
        print(f"\nTotal Income: ${total_income:.2f}")
        print(f"Total Expenses: ${total_expense:.2f}")
        print(f"Remaining Budget: ${remaining:.2f}")
    except FileNotFoundError:
        print("No transactions found!")

# Main program loop
def main():
    initialize_file()
    while True:
        print("\n=== Budget Tracker ===")
        print("1. Add Income/Expense")
        print("2. View Transactions")
        print("3. View Budget Summary")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == '1':
            add_transaction()
        elif choice == '2':
            view_transactions()
        elif choice == '3':
            calculate_budget()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please enter 1-4.")

# Run the program
if __name__ == "__main__":
    main()