
total_balance = int(input("Enter the total Balance: ₹"))

class Source:
    def __init__(self, income=0, expense=0):
        self.income = income
        self.expense = expense

class Category:
    def __init__(self, food=0, clothes=0, grocery=0, transport=0):
        self.food = food
        self.clothes = clothes
        self.grocery = grocery
        self.transport = transport


source_data = Source()
data = Category()

while True:
    print("\n==== Money Manager ====")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. Summary of Bank Statements")
    print("4. Exit")

    choice = int(input("Enter the choice: "))

    
    if choice == 1:
        amount = int(input("Enter the income: ₹"))
        source_data.income += amount
        total_balance += amount
        print("Income Added!")

   
    elif choice == 2:
        print("\nSelect Expense Category:")
        print("1. Food")
        print("2. Clothes")
        print("3. Grocery")
        print("4. Transport")
        cat_choice = int(input("Enter choice: "))
        amount = int(input("Enter expense amount: ₹"))

        if amount > total_balance:
            print("Not enough balance!")
            continue

        if cat_choice == 1:
            data.food += amount
        elif cat_choice == 2:
            data.clothes += amount
        elif cat_choice == 3:
            data.grocery += amount
        elif cat_choice == 4:
            data.transport += amount
        else:
            print("Invalid Category!")
            continue

        source_data.expense += amount
        total_balance -= amount
        print("Expense Added!")

  
    elif choice == 3:
        print("\n--- Bank Statement Summary ---")
        print(f"Total Income: ₹{source_data.income}")
        print(f"Total Expense: ₹{source_data.expense}")
        print(f"Remaining Balance: ₹{total_balance}")
        print("\nExpense Breakdown:")
        print(f"Food: ₹{data.food}")
        print(f"Clothes: ₹{data.clothes}")
        print(f"Grocery: ₹{data.grocery}")
        print(f"Transport: ₹{data.transport}")

    elif choice == 4:
        print("Exiting Money Manager...")
        break

    else:
        print("Invalid choice! Please try again.")
