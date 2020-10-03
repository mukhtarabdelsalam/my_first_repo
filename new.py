import random


def main():
    words = ["apple", "duplex", "banjo", "bookworm", "beekeeper"]
    word = random.choice(words)
    hidden_word = "_ " * len(word)
    print(hidden_word)
    lives = 8
    used_letters = ""

    while lives > 0:
        print("you have used the letters:", used_letters)
        guessed_letter = input("enter a letter\n")
        used_letters += guessed_letter + " "

        new_hidden = ""
        lose_life = True
        for i, character in enumerate(word):
            if guessed_letter.lower() == character:
                new_hidden += character + ""
                lose_life = False
            else:
                new_hidden += hidden_word[i*2] + " "

        if lose_life:
            lives = lives - 1

        hidden_word = new_hidden
        print(hidden_word)
        print("lives:", lives)

        if "_" not in hidden_word:
            print("you did it!!!")
            break

if __name__ == '__main__':
    main()
