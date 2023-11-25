import os

# Function to load expenses from the 'expenses.txt' file
def load_expenses():
    expenses = []
    if os.path.exists('expenses.txt'):
        with open('expenses.txt', 'r') as file:
            for line in file:
                date, description, amount = line.strip().split(',')
                expenses.append({'date': date, 'description': description, 'amount': float(amount)})
    return expenses

# Function to save expenses to the 'expenses.txt' file
def save_expenses(expenses):
    with open('expenses.txt', 'w') as file:
        for expense in expenses:
            file.write(f"{expense['date']},{expense['description']},{expense['amount']}\n")

# Function to display expenses in a formatted table
def display_expenses(expenses):
    print("Date       | Description       | Amount")
    print("---------------------------------------")
    for expense in expenses:
        print(f"{expense['date']} | {expense['description']:15} | ${expense['amount']:.2f}")

# Function to add a new expense to the list
def add_expense(expenses):
    try:
        date = input("Enter date (YYYY-MM-DD): ")
        description = input("Enter description: ")
        amount = float(input("Enter amount: $"))
        # Validation checks for input
        if not date or not description:
            raise ValueError("Date and description cannot be empty.")
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        expenses.append({'date': date, 'description': description, 'amount': amount})
        save_expenses(expenses)
        print("Expense added successfully!")
    except ValueError as e:
        print(f"Error: {e}")

# Function to edit an existing expense
def edit_expense(expenses):
    display_expenses(expenses)
    try:
        index = int(input("Enter the index of the expense to edit: ")) - 1
        if 0 <= index < len(expenses):
            expense = expenses[index]
            print("Editing Expense:")
            print(f"1. Date: {expense['date']}")
            print(f"2. Description: {expense['description']}")
            print(f"3. Amount: {expense['amount']}")
            choice = input("Enter the number of the field to edit (1/2/3): ")
            if choice == '1':
                expense['date'] = input("Enter new date (YYYY-MM-DD): ")
            elif choice == '2':
                expense['description'] = input("Enter new description: ")
            elif choice == '3':
                new_amount = float(input("Enter new amount: $"))
                if new_amount <= 0:
                    raise ValueError("Amount must be greater than zero.")
                expense['amount'] = new_amount
            else:
                raise ValueError("Invalid choice.")
            save_expenses(expenses)
            print("Expense edited successfully!")
        else:
            print("Invalid index.")
    except ValueError as e:
        print(f"Error: {e}")
1
# Function to delete an existing expense
def delete_expense(expenses):
    display_expenses(expenses)
    try:
        index = int(input("Enter the index of the expense to delete: "))
        if 0 <= index < len(expenses):
            del expenses[index]
            save_expenses(expenses)
            print("Expense deleted successfully!")
        else:
            print("Invalid index.")
    except ValueError:
        print("Invalid input. Please enter a valid index.")

# Main function to run the expense tracker
def main():
    print("Simple Expense Tracker")
    expenses = load_expenses()

    while True:
        print("\n1. View Expenses")
        print("2. Add Expense")
        print("3. Edit Expense")
        print("4. Delete Expense")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            display_expenses(expenses)
        elif choice == '2':
            add_expense(expenses)
        elif choice == '3':
            edit_expense(expenses)
        elif choice == '4':
            delete_expense(expenses)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")

if __name__ == "__main__":
    main()
