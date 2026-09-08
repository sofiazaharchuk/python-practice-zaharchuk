print("Sofia Zaharchuk, IT-32")

y = 2008


def print_age(year):
    age = 2026 - year
    print(f"Age: {age}")


def get_age(year, current_year=2026):
    if year > current_year or year < 0:
        return -1
    age = current_year - year
    return age
    print("after return")   # never executes, function already exited


print_age(y)

result = print(print_age(y))
print(f"print_age returned: {result}")

age = get_age(y)
print(f"Age from get_age: {age}")

print(f"Age in months: {age * 12}")
print(f"Age in weeks: {age * 52}")

age_in_2030 = get_age(y, 2030)
print(f"Age in 2030: {age_in_2030}")

invalid_result = get_age(3000)
print(f"Invalid year 3000 gives: {invalid_result}")

print("--- trying print_age(y) * 12 ---")
try:
    result2 = print_age(y) * 12
except TypeError as e:
    print(f"Error: {e}")
