import random
import string

print("H A N G M A N")

def play_game():
    computer_choice = random.choice(('python', 'java', 'kotlin', 'javascript'))
    answer_string = "-" * len(computer_choice)
    attempts = 8
    typed_letters = []

    while attempts > 0:
        print()
        print(answer_string)

        letter = input("Input a letter: ")

        if len(letter) == 1 and letter in string.ascii_lowercase:
            if letter in typed_letters:
                print("You already typed this letter")
            elif letter not in computer_choice:
                print("No such letter in the word")
                typed_letters.append(letter)
                attempts -= 1
            elif letter in computer_choice and letter in answer_string:
                print("No improvements")
                attempts -= 1
            else:
                i = 0
                while i < len(computer_choice):
                    if computer_choice[i] == letter:
                        answer_list = list(answer_string)
                        answer_list[i] = letter
                        answer_string = "".join(answer_list)
                        typed_letters.append(letter)
                        if answer_string == computer_choice:
                            print(f"You guessed the word {computer_choice}!\nYou survived!")
                            attempts = 0
                    i += 1

        elif len(letter) != 1:
            print("You should input a single letter")

        elif letter not in string.ascii_lowercase:
            print("It is not an ASCII lowercase letter")


    if answer_string != computer_choice:
        print("You are hanged!")

def options():
    choice = input('Type "play" to play the game, "exit" to quit: ')
    if choice == "play":
        play_game()
        print()
        options()
    elif choice == "exit":
        return

options()