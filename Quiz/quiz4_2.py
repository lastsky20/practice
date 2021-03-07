from random import *
words = ["apple","orange","banana"]
word = choice(words)
letters = ""


while True:
    clear = True
    print(word)
    for w in word:
        if w in letters:
            print(w, end="")
        else:
            print("_", end=" ")
            clear = False
    print()

    if clear:
        print("Game Over")
        break

    letter = input("Input word >")
    if letter not in letters:
        letters += letter

    if letter in word:
        print("correct!")
    else:
        print("Wrong!")




