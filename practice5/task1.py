print("Sofia Zaharchuk, IT-32")


def print_card():
    print(f"Name: Sofia Zaharchuk")
    print(f"Group: IT-32")
    print(f"Birth year: 2008")


def print_card_args(name, surname, year, group="IT-32"):
    print(f"{name} {surname}, {group}, {year}")


for i in range(1, 4):
    print(f"--- no parameters, call {i} ---")
    print_card()

print("--- positional arguments ---")
print_card_args("Sofia", "Zaharchuk", 2008, "IT-32")

print("--- keyword arguments ---")
print_card_args(year=2008, group="IT-32", name="Sofia", surname="Zaharchuk")

print("--- mixed arguments ---")
print_card_args("Sofia", "Zaharchuk", year=2008, group="IT-32")

print("--- default group ---")
print_card_args("Sofia", "Zaharchuk", 2008)

print("--- missing arguments error ---")
try:
    print_card_args("Sofia")
except TypeError as e:
    print(f"Error: {e}")

