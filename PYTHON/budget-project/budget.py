class Category:
    def __init__(self, name):
        # Initialize a category with a name and an empty ledger
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=''):
        # Add a deposit entry to the ledger
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=''):
        # Attempt to withdraw an amount if sufficient funds are available
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False

    def get_balance(self):
        # Calculate the current balance by summing all amounts in the ledger
        return sum(item['amount'] for item in self.ledger)

    def transfer(self, amount, category):
        # Transfer an amount to another category if sufficient funds are available
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {category.name}')
            category.deposit(amount, f'Transfer from {self.name}')
            return True
        return False

    def check_funds(self, amount):
        # Check if the amount is less than or equal to the current balance
        return amount <= self.get_balance()

    def __str__(self):
        # Create a string representation of the category ledger
        title = f"{self.name:*^30}\n"  # Center the category name within 30 characters, padded with '*'
        items = ''
        for entry in self.ledger:
            # Format each ledger entry with description and amount
            desc = entry['description'][:23]  # Truncate description to 23 characters
            amt = f"{entry['amount']:.2f}"[:7]  # Format amount to 2 decimal places, truncate to 7 characters
            items += f"{desc:<23}{amt:>7}\n"  # Align description left and amount right
        total = f"Total: {self.get_balance():.2f}"  # Add the total balance
        return title + items + total


def create_spend_chart(categories):
    # Create a bar chart showing the percentage of spending by category
    title = "Percentage spent by category\n"  # Chart title
    
    # Step 1: Calculate total withdrawals
    total_spent = 0  # Initialize total spent
    spent_per_category = []  # List to store spending per category
    for cat in categories:
        # Sum all negative amounts (withdrawals) for each category
        spent = sum(-item['amount'] for item in cat.ledger if item['amount'] < 0)
        spent_per_category.append(spent)  # Add spending to the list
        total_spent += spent  # Add to total spent

    # Step 2: Calculate percentage spent
    percentages = [int((spent / total_spent) * 10) * 10 for spent in spent_per_category]
    # Convert spending to percentages rounded down to the nearest 10

    # Step 3: Build chart from 100 to 0
    chart = ""
    for i in range(100, -1, -10):  # Iterate from 100% to 0% in steps of 10
        chart += f"{i:>3}|"  # Add percentage label
        for percent in percentages:
            # Add 'o' if the percentage is greater than or equal to the current level
            chart += " o " if percent >= i else "   "
        chart += " \n"  # Add a newline after each row

    # Step 4: Bottom line
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"
    # Add a horizontal line below the chart

    # Step 5: Vertical names
    max_len = max(len(cat.name) for cat in categories)  # Find the longest category name
    for i in range(max_len):  # Iterate over each character index
        row = "     "  # Add initial spacing
        for cat in categories:
            name = cat.name
            # Add the character at the current index or a space if the name is shorter
            row += f"{name[i] if i < len(name) else ' '}  "
        chart += row + "\n"  # Add the row to the chart

    return title + chart.rstrip('\n')  # Combine title and chart, removing the final extra newline



# Create a "Food" category
food = Category("Food")
# Deposit $1000 into the "Food" category with a description
food.deposit(1000, "initial deposit")
# Withdraw $10.15 from the "Food" category for groceries
food.withdraw(10.15, "groceries")
# Withdraw $15.89 from the "Food" category for restaurant expenses
food.withdraw(15.89, "restaurant and more food for dessert")

# Create a "Clothing" category
clothing = Category("Clothing")
# Deposit $500 into the "Clothing" category with a description
clothing.deposit(500, "initial deposit")
# Withdraw $25.55 from the "Clothing" category for a shirt
clothing.withdraw(25.55, "shirt")
# Withdraw $100 from the "Clothing" category for jeans
clothing.withdraw(100, "jeans")

# Create an "Auto" category
entertainment = Category("Auto")
# Deposit $1000 into the "Auto" category with a description
entertainment.deposit(1000, "initial deposit")
# Withdraw $15 from the "Auto" category for a movie
entertainment.withdraw(15, "movie")
# Withdraw $100 from the "Auto" category for a concert
entertainment.withdraw(100, "concert")

# Transfer $50 from the "Food" category to the "Clothing" category
food.transfer(50, clothing)

# Print the ledger of the "Food" category
print(food)
print()  # Print a blank line for separation
# Print the spending chart for the "Food", "Clothing", and "Auto" categories
print(create_spend_chart([food, clothing, entertainment]))
