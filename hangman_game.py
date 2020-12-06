#------------------------------------HANGMAN----------------------------------------
import random

# the list of words that the program will choose randomly one word each game
words = ["CAT", "APPLE", "ORANGE", "BATMAN",
         'IRONMAN', 'WONDERWOMEN', 'ALICE', 'MOTHER', 'BROTHER',
         'FATTHER', 'SISTER', 'YAER', 'MOUSE', 'COMPUTER', 'PHONE', 
         'NUMBER', 'TOWER', 'HAPPY', 'SPIDERMAN', 'COUNTRY', 'WOMAN', 
         'CONGRATULATION', 'ASSOCIATION', 'SCHOOLBUS']
current_word = random.choice(words)
current_word_list = list(current_word)
current_word_hidden = ["_" for letter in current_word]
# the list of letters (the length == 1) that the user guessed either they are in the current word or not
guessed_letters = []
# the list of words (that have the same length as the current word) that the user guessed either they are in the current word or not
guessed_words = []
# the list of words (length != 1 or length != len(current_word)) that the user guessed either they are in the current word on not
random_words = []
remain_tries = 7
game_stile_going = True
state_winning = None
# the board of hangman that will be shown on the screen depending on the remain_tries variable
board = [
        """
        ________
        |      |
        |      O
        |     \\|/
        |      |
        |     / \\
       _|_
        """,
        """
        ________
        |      |
        |      O
        |     \\|/
        |      |
        |     / 
       _|_
        """,
        """
        ________
        |      |
        |      O
        |     \\|/
        |      |
        |      
       _|_
        """,
        """
        ________
        |      |
        |      O
        |     \\|/
        |      
        |      
       _|_
        """,
        """
        ________
        |      |
        |      O
        |     \\|
        |      
        |      
       _|_
        """,
        """
        ________
        |      |
        |      O
        |      |
        |      
        |      
       _|_
        """,
        """
        ________
        |      |
        |      O
        |     
        |      
        |     
       _|_
        """,
        """
        ________
        |      |
        |      
        |     
        |      
        |     
       _|_
        """
    ]


def display_board():
    print(f"You have {remain_tries} tries to guess the word")
    print(board[remain_tries])
    word_to_be_guessed = " ".join(current_word_hidden)
    print(word_to_be_guessed)
    print()


def handle_turn():
    global remain_tries
    global current_word_hidden
    player = input("Guess a letter or the whole word: ").upper()
    if len(player) == 1:
        if player in guessed_letters:
            print("You already guessed that letter")
        elif player not in guessed_letters:
            if player in current_word_list:
                for index, letter in enumerate(current_word_list):
                    if letter == player:
                        current_word_hidden[index] = letter
                        guessed_letters.append(letter)
                display_board()
            elif player not in current_word_list:
                print(f"{player} not found")
                guessed_letters.append(player)
                remain_tries -= 1
                display_board()
    elif len(player) == len(current_word):
        if player in guessed_words:
            print("You already guessed that word")
        elif player not in guessed_words:
            if player == current_word:
                current_word_hidden = list(player)
                display_board()
            elif player != current_word:
                print(f"{player}, is not the word.")
                guessed_words.append(player)
                remain_tries -= 1
                display_board()
    elif len(player) == 0:
        print('Please enter a letter or a word!')
    else:
        if player in random_words:
            print("You already guessed that word")
        if player not in random_words:
            random_words.append(player)
            remain_tries -= 1
            display_board()


def check_winner():
    global game_stile_going
    global state_winning
    if current_word_list == current_word_hidden:
        game_stile_going = False
        state_winning = "WON"


def check_loser():
    global game_stile_going
    global state_winning
    if remain_tries == 0:
        game_stile_going = False
        state_winning = "TIE"


def check_game_over():
    check_winner()
    check_loser()


def playing_game():
    display_board()
    while game_stile_going:
        handle_turn()
        check_game_over() 
    if state_winning == "WON":
        print("Congratulations, You won")
        print()
        play_again()
    elif state_winning == "TIE":
        print(f"The word is: {current_word}.")
        print("Maybe next time.")
        print()
        play_again()


def play_again():
    global current_word
    global current_word_list
    global current_word_hidden
    global guessed_letters
    global guessed_words
    global random_words
    global remain_tries
    global game_stile_going
    global state_winning
    print("Do you want to play agian (Yes/No)")
    answer = input(">>>> ").upper()
    if answer in ["yes", "YES", "y", "Y"]:
        current_word = random.choice(words)
        current_word_list = list(current_word)
        current_word_hidden = ["_" for letter in current_word]
        guessed_letters = []
        guessed_words = []
        random_words = []
        remain_tries  = 7
        game_stile_going = True
        state_winning = None
        playing_game()
    elif answer in ["NO", "no", "n", "N"]:
        return


playing_game()






