def add_expense(expenses, amount, category):
    # Adds a new expense to the list of expenses
    expenses.append({'amount': amount, 'category': category})
    
def print_expenses(expenses):
    # Prints all expenses in the list
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')
    
def total_expenses(expenses):
    # Calculates the total amount of all expenses
    return sum(map(lambda expense: expense['amount'], expenses))
    
def filter_expenses_by_category(expenses, category):
    # Filters expenses by a specific category
    return filter(lambda expense: expense['category'] == category, expenses)
    

def main():
    # Main function to run the expense tracker program
    expenses = []  # Initialize an empty list to store expenses
    while True:
        # Display menu options to the user
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')
       
        choice = input('Enter your choice: ')  # Get user input for menu choice

        if choice == '1':
            # Add a new expense
            amount = float(input('Enter amount: '))  # Get the expense amount
            category = input('Enter category: ')  # Get the expense category
            add_expense(expenses, amount, category)

        elif choice == '2':
            # List all expenses
            print('\nAll Expenses:')
            print_expenses(expenses)
    
        elif choice == '3':
            # Show the total of all expenses
            print('\nTotal Expenses: ', total_expenses(expenses))
    
        elif choice == '4':
            # Filter expenses by a specific category
            category = input('Enter category to filter: ')  # Get the category to filter by
            print(f'\nExpenses for {category}:')
            expenses_from_category = filter_expenses_by_category(expenses, category)
            print_expenses(expenses_from_category)
    
        elif choice == '5':
            # Exit the program
            print('Exiting the program.')
            break