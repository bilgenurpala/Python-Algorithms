'''
1. Get total income from the user.

2. Get total expenses from the user.

3. Calculate the remaining amount: remaining = income - expenses.

4. If remaining is positive → print profit.

5. If remaining is negative → print loss.

6. If remaining is zero → print break-even.
'''

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