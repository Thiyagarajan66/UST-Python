"""Python is a popular programming language.
It was created by Guido van Rossum, and released in 1991."""


vowels = ['a', 'e', 'i', 'o', 'u']
passage = ("Python is a popular programming language. It was created by Guido van Rossum, and released in 1991.")

vowel = 0
consonants = 0

for x in passage:
    if x in vowels:
        vowel += 1
    elif x != ' ':
        consonants += 1

print("Vowels: ", vowel)
print("Consonants: ", consonants)
