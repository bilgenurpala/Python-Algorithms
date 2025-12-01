'''
1. Ask the user to enter the original product price.
2. Ask the user to enter the discount percentage.
3. Convert the percentage into a decimal and calculate the discount amount.
4. Subtract the discount amount from the original price to get the new price.
5. Display the original price, the discount rate, the discount amount, and the final price.
6. Show how much money the user saves.

'''

print("=== Discount Calculator ===")

price = float(input("Enter product price: "))
discount = float(input("Enter discount percentage: "))

discount_amount = price * (discount / 100)
new_price = price - discount_amount

print(f"\nOriginal Price: {price}")
print(f"Discount: {discount}%")
print(f"Discount Amount: {discount_amount}")
print(f"New Price: {new_price}")
print(f"You save: {discount_amount}")