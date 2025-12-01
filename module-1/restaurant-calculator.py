'''
1. Ask the user to enter the food price.
2. Ask the user to enter the tip percentage.
3. Ask the user to enter the number of people.
4.Calculate the tip amount using the percentage.
5. Add the tip to the food price to get the total bill.
6. Divide the total bill by the number of people to find the cost per person.
7. Display the food price, tip amount, total bill, number of people, and the per-person payment.

'''
print("=== Restaurant Bill Calculator ===")

food_price = float(input("Enter food price: "))
tip_percentage = float(input("Enter tip percentage: "))
number_of_people = int(input("Enter number of people: "))

tip_amount = food_price * (tip_percentage / 100)
total = food_price + tip_amount
per_person = total / number_of_people

print(f"\nFood Price: {food_price}")
print(f"Tip ({tip_percentage}%): {tip_amount}")
print(f"Total Bill: {total}")
print(f"Number of People: {number_of_people}")
print(f"Per Person: {per_person:.2f}")