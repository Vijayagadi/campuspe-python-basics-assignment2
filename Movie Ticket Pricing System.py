age = int(input("Enter age: "))
day = input("Enter day of week: ")
tickets = int(input("Enter number of tickets: "))

# Age based price
if age < 3:
    price = 0
elif age <= 12:
    price = 150
elif age <= 59:
    price = 300
else:
    price = 200

# Day based discount
if day.lower() in ["friday", "saturday", "sunday"]:
    discount = price * 0.20
else:
    discount = 0

final_price = price - discount
total_amount = final_price * tickets

print("\nBase price:", price)
print("Discount per ticket:", discount)
print("Price after discount:", final_price)
print("Total amount:", total_amount)