sentence = input("Enter a sentence: ")
print("\nOriginal:", sentence)
print("Characters (with spaces):", len(sentence))
print("Characters (without spaces):", len(sentence.replace(" ", "")))

words = sentence.split()
print("Number of words:", len(words))

print("Uppercase:", sentence.upper())
print("Lowercase:", sentence.lower())

if words:
    print("First word:", words[0])
    print("Last word:", words[-1])

print("Reversed:", sentence[::-1])