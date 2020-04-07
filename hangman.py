import random

name = input("Your Name: ")
print("Welcome to hangman game " + name + "!")

word_list = ["Metallica","Queen","Radiohead","Pink Floyd","Foo Fighters"]
guess_stirng = ""
random.shuffle(word_list)
word = word_list[0]
lives = 5

while lives > 0:
    chracter_left = len(word)
    for chracter in word:
        if chracter in guess_stirng:
            print(chracter)
            chracter_left -= 1
        else:
            print("-")
    if chracter_left == 0:
        print("You Win!!")
        break

    guess = input("Guess a letter: ")
    guess_stirng += guess
    if guess not in word:
        lives -= 1
        if lives == 0:
            print("You died!")
            break
        else:
            print(f"Wrong guess! You have only {lives} lives left")






