"""
First test for generating sentences
Unit 2 Project
"""

import pprint
import random

file = open("love_lucy_corpus.txt", "r")

markov = {}

words = file.read().replace("\n", " ").split()

i = 0
while i < len(words) - 1:
    word = words[i]
    next_word = words[i + 1]

    if word in markov:
        markov[word].append(next_word)
    else:
        markov[word] = [next_word]

    i = i + 1

# Prompt the user for a word:
word = input("Enter a word to start a sentence: ")

# Do some error checking
while word not in markov:
    word = input("Your word was not in my corpus. Please try again: ")

output = word

while not output.endswith("."):
    next_word = random.choice(markov[word])
    output = output + (" " + next_word)
    word = next_word

print(output)
