print("Sofia Zaharchuk, IT-32")

name = "Sofia"
surname = "Zaharchuk"


def get_initials(name: str, surname: str) -> str:
    return f"{name[0]}.{surname[0]}."


def count_letters(text: str, letter: str = "a") -> int:
    """Return how many times letter occurs in text."""
    count = 0
    for character in text:
        if character.lower() == letter.lower():
            count += 1
    return count


def count_vowels(text: str) -> int:
    vowels = 0
    for character in text:
        if character.lower() in "aeiouy":
            vowels += 1
    return vowels


def reverse_text(text: str) -> str:
    result = ""
    for character in text:
        result = character + result
    return result


print(f"Full name: {name} {surname}")
print(f"Initials: {get_initials(name, surname)}")

letters_count = len(surname)
vowels_count = count_vowels(surname)
consonants_count = letters_count - vowels_count

print(f"Letters in surname: {letters_count}")
print(f"Vowels: {vowels_count}, consonants: {consonants_count}")

for vowel in "aeiou":
    print(f"{vowel}: {count_letters(surname, letter=vowel)}")

print(f"Default letter 'a': {count_letters(surname)}")

print(f"Reversed surname: {reverse_text(surname)}")

print(f"Docstring: {count_letters.__doc__}")
print(f"Annotations: {count_letters.__annotations__}")
