from bee_solver import words, anagram
from random import choice, shuffle

def scramble(word):
    word = list(word)
    shuffle(word)
    return ''.join(word)

f = open('pangrams.txt','r')

pangram = scramble(set(choice(f.readlines()).strip()))
centre = choice(pangram).strip()

print("Pangram: {}\nCentre: {}".format(pangram,centre))

solutions = words(pangram,centre)
print(solutions)