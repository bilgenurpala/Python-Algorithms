'''
1. Ask the user to enter their birth year, month, and day.
2. Create a birth date object using the given values.
3. Get today’s date from the system.
4. Calculate the time difference between today and the birth date.
5. Extract the number of days from this difference.
6. Display how many days the user has lived.
7. Also print the birth date and today’s date together with the total number of days.
'''

from datetime import datetime
print("===== Age Calculator =====")
birth_year = int(input("Enter your birth year (YYYY): "))
birth_month = int(input("Enter your birth month (MM): "))
birth_day = int(input("Enter your birth day (DD): "))
birth_date = datetime(birth_year, birth_month, birth_day)
today = datetime.now()
age_days = (today - birth_date).days
print(f"You have lived for {age_days} days.")
print(f"From {birth_date.date()} to {today.date()} is {age_days} days.")