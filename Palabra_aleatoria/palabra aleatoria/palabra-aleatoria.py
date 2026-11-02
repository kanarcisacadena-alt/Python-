"""import random

word = input("Enter a word: ")

abc = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

for c in range(len(word)):
    if word[c].isalpha():
        random_letter = random.choice(abc)
        print(random_letter, end="")
    else:
        print(word[c], end="")"""


def a():
    print('Start of a()')
    b()  # Call b().

def b():
    print('Start of b()')
    c()  # Call c().

def c():
    print('Start of c()')
    42 / 0  # This will cause a zero divide error.
    a()  # Call a().