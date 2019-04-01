import sys

def game_over():
    print("""You lost!
' _________ '
'|    |    |'
'|  \ 0 /  |'
'|    |    |'
'|    |    |'
'|   / \\   |'
' _________ '""" + '\n')

def hangman(clue_word):
    tries = 10
    guess_arr = ["_"] * len(clue_word)
    print("Welcome to Hangman! Let's play!")

    while tries:
        guess_str = ''.join(map(str, guess_arr))
        print(guess_str + '\n') 
        guess_letter = str(input("Guess a letter: "))

        if guess_letter in clue_word:
            for index in range(len(guess_arr)):
                if clue_word[index] == guess_letter:
                    guess_arr[index] = guess_letter
                    guess_str = ''.join(map(str, guess_arr))
                    if guess_str == clue_word:
                        return '\n' + clue_word + '\n' + "Congratulations!"
        else:
            print("Incorrect!")
            tries -= 1
            if tries == 0:
                game_over()
                sys.exit()

if __name__ == "__main__":
    print(hangman("непротивоконституционствувателствуващите"))