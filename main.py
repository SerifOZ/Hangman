import random

global word_list
word_list = []


def create_list(word):
    for i in word:
        word_list.append("_")
    return word_list


def check_answer():
    temp = 0
    for i in word_list:
        if i == "_":
            temp += 1
    if temp != 0:
        return False
    else:
        return True


def check_letter(letter, word):
    if word.count(letter) > 0:
        return True
    else:
        return False


def print_word(word, letter):
    for i in range(0, len(word)):
        if word[i] == letter:
            word_list[i] = letter
    return word_list


def game_starting(word):
    create_list(word.lower())
    play_game(word.lower())


def play_game(word):
    false_answer = 0
    print("Welcome to hangman game...")
    while not check_answer():
        letter = input("\nChoose one letter : ")
        if check_letter(letter, word):
            print_word(word, letter)
            for i in word_list:
                print(i, end='')
        else:
            false_answer += 1
            print(f"You choose false letter.\nYou left {6-false_answer} chooses")
        if false_answer == 6:
            print("You lost")
            break
    if check_answer():
        print("\nYou win")

words = ["Hangman", "Hello", "Şerif", "Python", "Pamukkale"]
game_starting(random.choice(words))
