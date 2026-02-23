def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

def modulus(a, b):
    return a % b

def power(a, b):
    return a ** b


while True:
    print("\n1.Add 2.Subtract 3.Multiply 4.Divide 5.Modulus 6.Power 7.Exit")
    choice = int(input("Enter choice: "))

    if choice == 7:
        break

    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))

    if choice == 1:
        print("Result:", add(x, y))
    elif choice == 2:
        print("Result:", subtract(x, y))
    elif choice == 3:
        print("Result:", multiply(x, y))
    elif choice == 4:
        print("Result:", divide(x, y))
    elif choice == 5:
        print("Result:", modulus(x, y))
    elif choice == 6:
        print("Result:", power(x, y))
    else:
        print("Invalid choice")