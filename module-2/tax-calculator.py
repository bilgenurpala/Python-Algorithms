'''
1. Ask the user to enter their annual income.
2. Check the income range and determine the corresponding tax rate.
3. Calculate the tax amount based on the chosen tax rate.
4. Subtract the tax amount from the income to find the net income.
5. Display the gross income, tax rate, tax amount, and net income.

'''

print("=== Tax Calculator ===")

income = float(input("Enter your annual income: "))

if income <= 10000:
    tax_rate = 0
    tax = 0
elif income <= 30000:
    tax_rate = 10
    tax = income * 0.10
elif income <= 60000:
    tax_rate = 20
    tax = income * 0.20
elif income <= 100000:
    tax_rate = 30
    tax = income * 0.30
else:
    tax_rate = 40
    tax = income * 0.40

net_income = income - tax

print(f"\nGross Income: {income}")
print(f"Tax Rate: {tax_rate}%")
print(f"Tax Amount: {tax}")
print(f"Net Income: {net_income}")