birth_year = int(input("Enter your birth year: "))
current_year = 2025
age = current_year - birth_year
months = age * 12
days = age * 365
hours = days * 24
minutes = hours * 60
years_to_100 = 100 - age
print("\nYour current age is:", age, "years")
print("Your age in months:", months)
print("Your age in days (approx):", days)
print("Your age in hours:", hours)
print("Your age in minutes:", minutes)
if years_to_100 > 0:
    print("Years left to reach 100:", years_to_100)
else:
    print("You are already 100 or more!")