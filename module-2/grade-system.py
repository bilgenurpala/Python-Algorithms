'''
1. Ask the user to enter a grade between 0 and 100.
2. Compare the grade with the defined score ranges.
3. Assign the correct letter grade (A, B, C, D, or F).
4. Determine if the student passed or failed.
5. Display the numeric grade, the letter grade, and the pass/fail status.

'''
print("=== Pass/Fail Grade System ===")

grade = float(input("Enter your grade (0-100): "))

if grade >= 90:
    letter = "A"
    status = "Passed"
elif grade >= 80:
    letter = "B"
    status = "Passed"
elif grade >= 70:
    letter = "C"
    status = "Passed"
elif grade >= 60:
    letter = "D"
    status = "Passed"
else:
    letter = "F"
    status = "Failed"

print(f"\nYour grade: {grade}")
print(f"Letter grade: {letter}")
print(f"Status: {status}")