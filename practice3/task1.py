print("Sofia Zaharchuk, IT-32")

name = input("Enter your name: ")

if not name:
    print("No name entered, using default")
    name = "Anonymous"

age = int(input("Enter your age (integer): "))

if age < 0:
    category = "invalid value"
elif age <= 6:
    category = "child"
elif age <= 17:
    category = "schoolchild"
elif age <= 64:
    category = "adult"
else:
    category = "senior"

print(f"Hello, {name}! Your category is: {category}")
