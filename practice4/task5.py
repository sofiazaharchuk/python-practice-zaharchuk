print("Sofia Zaharchuk, IT-32")

d = 6
c = 9
n = d * c

print(f"n = {d} * {c} = {n}")

divisors_count = 0
divisors_sum = 0

print("Divisors:", end=" ")
for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")
        divisors_count += 1
        divisors_sum += i
print()

print(f"Divisors count: {divisors_count}, sum: {divisors_sum}")

for divisor in range(2, n):
    if n % divisor == 0:
        print(f"{n} is not prime: divisible by {divisor}")
        break
else:
    print(f"{n} is prime")

primes_count = 0
print(f"Primes up to {n}:", end=" ")
for candidate in range(2, n + 1):
    is_prime = True
    for divisor in range(2, candidate):
        if candidate % divisor == 0:
            is_prime = False
            break
    if is_prime:
        print(candidate, end=" ")
        primes_count += 1
print()

print(f"Primes count: {primes_count}")
