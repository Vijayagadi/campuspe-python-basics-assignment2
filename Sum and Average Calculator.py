count = int(input("How many numbers? "))

total = 0
maximum = None
minimum = None

for i in range(count):
    n = int(input("Enter number: "))
    total = total + n

    if maximum is None or n > maximum:
        maximum = n

    if minimum is None or n < minimum:
        minimum = n

average = total / count

print("\nSum:", total)
print("Average:", average)
print("Maximum:", maximum)
print("Minimum:", minimum)