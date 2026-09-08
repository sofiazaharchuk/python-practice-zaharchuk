print("Sofia Zaharchuk, IT-32")

name = "Sofia"
surname = "Zaharchuk"
full_name = name + surname

vowels_count = 0
consonants_count = 0

for character in full_name:
    if character.lower() in "aeiouy":
        vowels_count += 1
    else:
        consonants_count += 1

print(name + " " + surname)
print(f"Vowels: {vowels_count}, consonants: {consonants_count}")
print(f"Total letters: {len(full_name)}")
