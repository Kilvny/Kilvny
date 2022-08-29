from os import remove
import random
from words import words
import string
from hangsman_graphics import lives_visual_dict 
from hangsman_graphics import won_visual
from hangsman_graphics import lost_visual

# define a function to valdiate the words without spaces without invalid characters

def validate(words):
    word=random.choice(words)
    while "-" in word or " " in word:
        word=random.choice(words)
    return word.upper()

def hangman():
    
    word=validate(words)
    word_letters = set(word) # put the random word in a set
    used_letters = set() # to keep track of user entered letters
    alphabet = (string.ascii_uppercase)
    lives = 8
    print("""
    Wecome to the game, developed by Kilvny 2022 C 
    Rules:
    I will give you a random word and you will get 8 lives to guess the word 
    Other than that.. your man is going to meet his fate! 
    
                Good Luck ... :k
    """)
    # getting users input 
    while len(word_letters) > 0:
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Word letters you've guessed: ", " ".join(word_list))
        guess=input("Guess a letter : ")
        guess=guess.upper()
        
        if len(guess) > 1 or guess not in alphabet: # to make sure it's an alphabet charcter
            print("\nThis is not a letter!")
            continue
        if guess not in used_letters:
            used_letters.add(guess)
            if guess in word_letters:
                word_letters.remove(guess)
            else: 
                print("wrong char :( ")
                lives -=1 # decreamnt a a live

        elif guess not in word_letters and guess in used_letters:
            print("your already used that char!")
            lives -=1 # decreamnt a a live

        

        print("The letters you have used ", " ".join(used_letters))
        
        print(f"You only have {lives} lives left",f"{lives_visual_dict[lives]}")
        if lives == 0:
            break # gets here if used finished his trials so he lost and the loop breaks
    # get's here when loop ends when lenth of word_letters == 0
    if lives > 0:
        print(f"\n\ngood job! you won and guessed {word} correctly! ".upper())
        print(won_visual["won"])
    else:
        print("\n\nYOU'VE LOST", lost_visual["lost"],f"\n\nTHE WORD WAS: {word}")

    

if __name__ == '__main__':
    hangman()
