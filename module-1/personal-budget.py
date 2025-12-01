print("=== Personal Budget Calculator ===")

income = float(input("Enter your income: "))
expenses = float(input("Enter your expenses: "))

remaining = income - expenses

print(f"Income: {income}")
print(f"Expenses: {expenses}")
print(f"Remaining: {remaining}")

if remaining > 0:
    print("You have surplus!")
elif remaining < 0:
    print("You have deficit!")
else:
    print("Budget balanced!")