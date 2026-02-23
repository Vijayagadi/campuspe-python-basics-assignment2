total_bill = float(input("Enter total bill amount: "))
people = int(input("Enter number of people: "))
tax_percent = float(input("Enter tax percentage: "))
tip_percent = float(input("Enter tip percentage: "))

tax_amount = (total_bill * tax_percent) / 100
after_tax = total_bill + tax_amount

tip_amount = (after_tax * tip_percent) / 100
final_total = after_tax + tip_amount

per_person = final_total / people

print("\n=== BILL DETAILS ===")
print("Subtotal:", total_bill)
print("Tax amount:", tax_amount)
print("After tax:", after_tax)
print("Tip amount:", tip_amount)
print("Final total:", final_total)
print("Amount per person:", per_person)