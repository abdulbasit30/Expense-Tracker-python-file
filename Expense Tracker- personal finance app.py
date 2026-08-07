expensesList = [] #list of all dictionary expenses
print("Welcome to the Expense Tracker App! : Kharcha kam kiya kro, paisa bachao! 👀 ")
while True:
    print("\n -------MENU-------")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View all Expenses")
    print("4. Exit")
# 1. Add Expense
    choice = int(input("Please enter your choice:"))
    if choice == 1:
        date=input("Enter the date (YYYY-MM-DD): ")
        category=input("Enter the category (e.g., Food, Transport, Entertainment): ")
        description=input("Aur details do: ")
        amount=float(input("Enter the amount spent: "))

        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }
        expensesList.append(expense)
        print("\nExpense added successfully!")

# 2. View Expenses (list each expense)
    elif choice == 2:
        if len(expensesList) == 0:
            print("No expenses recorded yet. Jao pehly kharcha krein.")
        else:
            print("------Your Expenses------")
            count = 1
            for eachExpense in expensesList:
                print(f"Expense Number{count} --> {eachExpense["date"]}, {eachExpense["category"]},{eachExpense["description"]}, {eachExpense["amount"]}")

                count = count + 1

#3. View all Expenses
    elif choice == 3:
        total = 0
        for eachExpense in expensesList:
            total = total + eachExpense["amount"]

        print("\nTotal Expenses: ", total)

#4. Exit
    elif choice == 4:
        print("Thank you for using the Expense Tracker App! Goodbye! ☺")
        break

    else:
        print("Invalid choice. Please try again.")
