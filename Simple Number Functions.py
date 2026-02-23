def factorial(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def sum_digits(n):
    s = 0
    for d in str(n):
        s += int(d)
    return s

def reverse_num(n):
    return int(str(n)[::-1])

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Simple menu
while True:
    print("\n1.Factorial 2.Prime 3.SumDigits 4.Reverse 5.GCD 6.Exit")
    ch = int(input("Enter choice: "))

    if ch == 6:
        break

    if ch == 1:
        n = int(input("Enter number: "))
        print("Factorial:", factorial(n))

    elif ch == 2:
        n = int(input("Enter number: "))
        print("Prime:", is_prime(n))

    elif ch == 3:
        n = int(input("Enter number: "))
        print("Sum of digits:", sum_digits(n))

    elif ch == 4:
        n = int(input("Enter number: "))
        print("Reverse:", reverse_num(n))

    elif ch == 5:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("GCD:", gcd(a, b))

    else:
        print("Invalid choice")