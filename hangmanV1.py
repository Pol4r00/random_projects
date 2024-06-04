import random

options = ["BRAZIL","IRELAND","RUSSIA","SPAIN","CANADA","FRANCE","ITALY","ENGLAND","PORTUGAL","CHILE","SLOVENIA"]
deathcounter = 0
stringbuilder = []
list_of_choices = []
counter = 0

def check_letter(letterchoice,word_now,counter):
    global list_of_choices
    if letterchoice.upper() in list_of_choices:
        print("Letter already picked.")
    else:
        list_of_choices.append(letterchoice.upper())
    for letter in range(len(word_now)):
        global stringbuilder
        if letterchoice.upper() == word_now[letter]:
            stringbuilder[letter] = letterchoice.upper()
            counter = 1
    if counter == 0:
        global deathcounter
        deathcounter += 1

def random_word(word_now):
    global stringbuilder
    global joined
    for x in range(len(word_now)):
        stringbuilder.append("_")
    joined = "".join(stringbuilder)

word_now = random.choice(options)
print("HANGMAN")
random_word(word_now)
while True:
    print(" ".join(stringbuilder))
    print("Death counter:",deathcounter)
    print("Letters already picked: "," ".join(list_of_choices))
    letterchoice = input("Input your guess:")
    check_letter(letterchoice,word_now,counter)
    if deathcounter == 7:
        print("YOU DIED!")
        print("The word was",word_now)
        break
    if "_" not in stringbuilder:
        print(" ".join(stringbuilder))
        print("YOU WIN!")
        break
