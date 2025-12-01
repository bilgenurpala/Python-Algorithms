# 1.9 Ödev Önerileri (Assignment Suggestions) - Modül 1 (Module 1)

# 1. Basit Dönüştürücü (Simple Converter) = Create a converter program for Metre -> Feet and Kilogram -> Pound.
print("===== Basit Dönüştürücü (Simple Converter) =====")
print("1. Meter to Feet")
print("2. Feet to Meter")
print("3. Kilogram to Pound")
print("4. Pound to Kilogram")

choice = int(input("Select option (1-4): "))

if choice == 1:
    meter = float(input("Enter meter: "))
    feet = meter * 3.28084
    print(f"{meter} meter = {feet:.2f} feet")
elif choice == 2:
    feet = float(input("Enter feet: "))
    meter = feet / 3.28084
    print(f"{feet} feet = {meter:.2f} meter")
elif choice == 3:
    kg = float(input("Enter kilogram: "))
    pound = kg * 2.20462
    print(f"{kg} kg = {pound:.2f} pound")
elif choice == 4:
    pound = float(input("Enter pound: "))
    kg = pound / 2.20462
    print(f"{pound} pound = {kg:.2f} kg")
else:
    print("Invalid option!")

