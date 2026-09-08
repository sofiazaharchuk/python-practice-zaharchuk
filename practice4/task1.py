print("Sofia Zaharchuk, IT-32")

d = 6
c = 9

count = 0
total = 0
product = 1
even_count = 0
odd_count = 0

print(f"Numbers from {d} to 31:", end=" ")
for number in range(d, 32):
    print(number, end=" ")
    count += 1
    total += number
    product *= number
    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print()

average = total / count

print(f"Count: {count}")
print(f"Sum: {total}")
print(f"Product: {product}")
print(f"Average: {average:.2f}")
print(f"Even: {even_count}, odd: {odd_count}")

print("\n# while version")
count_w = 0
total_w = 0
product_w = 1
even_count_w = 0
odd_count_w = 0
number_w = d

print(f"Numbers from {d} to 31:", end=" ")
while number_w <= 31:
    print(number_w, end=" ")
    count_w += 1
    total_w += number_w
    product_w *= number_w
    if number_w % 2 == 0:
        even_count_w += 1
    else:
        odd_count_w += 1
    number_w += 1
print()

average_w = total_w / count_w

print(f"Count: {count_w}")
print(f"Sum: {total_w}")
print(f"Product: {product_w}")
print(f"Average: {average_w:.2f}")
print(f"Even: {even_count_w}, odd: {odd_count_w}")

print("\nCountdown:", end=" ")
for i in range(c, 0, -1):
    print(i, end=" ")
print()
