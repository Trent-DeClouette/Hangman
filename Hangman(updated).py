import os
import glob
import random
"""     
        Hangman
        Programed by Trent DeClouette
        28.November.2020
"""
with open('/Users/trent/OneDrive/Music/Documents/Python/python/Hangman/usa.txt') as f:
    lines = f.readlines()
    word = random.choice(lines)

temp = list("_ " * (len(word)-1))
print("".join(temp))

usedLetters = ""
lives = 6

def findOccurrences(str, chr):
    return [i for i, letter in enumerate(str) if letter == chr]

while lives > 0 and "_" in "".join(temp):

    userInput = input("Enter a letter\n")

    if userInput in word:
        for i in findOccurrences(word, userInput):
            temp[i * 2] = userInput
        print("".join(temp))
    else:
        lives -= 1
        print(userInput + " is not a letter in the word.\n" + str(lives) + " lives remaining.")

    usedLetters += userInput + " "
    print("Used Letters: " + usedLetters)
print("You win!" if "_" not in "".join(temp) else "The word was " + word + "\nYou loose!")
