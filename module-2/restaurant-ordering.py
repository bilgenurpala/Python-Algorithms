'''
1. Ask the user to enter their annual income.
2. Check the income range and determine the corresponding tax rate.   
3. Calculate the tax amount based on the chosen tax rate.
4. Subtract the tax amount from the income to find the net income.
5. Display the gross income, tax rate, tax amount, and net income.

'''

print("=== Restaurant Ordering System ===")
print("\n--- MENU ---")
print("1. Burger - $10")
print("2. Pizza - $15")
print("3. Pasta - $12")
print("4. Salad - $8")
print("5. Drink - $3")
print("0. Finish order")

total = 0
order_list = []

while True:
    choice = int(input("\nSelect item (0-5): "))
    
    if choice == 0:
        break
    elif choice == 1:
        total += 10
        order_list.append("Burger")
        print("Burger added!")
    elif choice == 2:
        total += 15
        order_list.append("Pizza")
        print("Pizza added!")
    elif choice == 3:
        total += 12
        order_list.append("Pasta")
        print("Pasta added!")
    elif choice == 4:
        total += 8
        order_list.append("Salad")
        print("Salad added!")
    elif choice == 5:
        total += 3
        order_list.append("Drink")
        print("Drink added!")
    else:
        print("Invalid choice!")

print("\n=== ORDER SUMMARY ===")
print("Items ordered:")
for item in order_list:
    print(f"- {item}")
print(f"\nTotal: ${total}")