text = input("Enter a word or number: ")

original = text
reverse = text[::-1]

print("Original:", original)
print("Reversed:", reverse)

if original.lower() == reverse.lower():
    print("Result: PALINDROME")
else:
    print("Result: NOT PALINDROME")