a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Choose an operation: ")

if choice == "1":
    print("Answer:", a + b)
elif choice == "2":
    print("Answer:", a - b)
elif choice == "3":
    print("Answer:", a * b)
elif choice == "4":
    print("Answer:", a / b)
else:
    print("Invalid choice")