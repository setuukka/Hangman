import random as random
from asciihangman import hangman_stages
from wordlist import words as words
import sys

guessed_letters = [] # stores already guessed letters
wordcount = len(words)


#print(hangman_stages[0])
def word_select(words):
    #select a random word from wordlist ny generating an integer between zero and number of words on list
    selected_word = words[random.randint(0, wordcount)]
    return selected_word

def checker(word: str, guess: str, state: str, stages: int):
    if guess not in guessed_letters:
        guessed_letters.append(guess)

    count = 0
    state = ""
    #this function takes the word and letter, checks if its in it and returs value based on that
    #Return value is a list like "_ _ a _ _ f _ _
    count = word.count(guess)
    if count == 1:
        print(f"There is {count} letter {guess}")
    elif count > 1:
        print(f"There are {count} letter {guess}")
    for letter in word:
        if letter in guessed_letters:
            state = state + letter + " "
        else:
            state = state + "_ "
    if "_" not in state:
        print()
        print()
        print("CONGRATULATIONS, YOU WON!!")
        print()
        print()
        print(f"The word was {state}!")
        sys.exit()
    if count == 0:
        stages += 1

    return state, stages

def start_game():
    stages = 0
    word = word_select(words) #import random word
    state = (f"{'_ '* len(word)}") # setting initial state to blank
    #print(word)
    print("Welcome to the HANGMAN!")
    while True:
        #print("stage:", stages)
        print("*******************************")
        print("Your progress looks like this: ")
        print(hangman_stages[stages])
        if stages == 7:
            print("GAME OVER")
            print(f"The word was {word}")
            break
        print(f"The word you are trying to guess is {len(word)} letters long")
        print()
        print(state)
        print()
        print(f"You have already guessed these letter: {guessed_letters}")
        guess = str(input("What letter do you want to guess? Two letters to quit: "))
        if len(guess) > 1:
            print("Thank you for playing!")
            break
        else:
            if guess not in guessed_letters:
                guessed_letters.append(guess)
                state, stages = checker(word, guess, state, stages)

            else:
                print("You have already guessed this letter. Try again: ")
def main():
    start_game()

main()