
def hangman():
    import string
    import random

    _LENGTH = 5
    string_pool = string.ascii_lowercase
    word = ""
    for i in range(_LENGTH):
        word += random.choice(string_pool)
        
    wrong = 0
    stages = ["",
              "-------          ",
              "|      |         ",
              "|      |         ",
              "|      0         ",
              "|     /|/        ",
              "|      //        ",
              "|                ",
              ]
    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    print("Welcome to Hangman")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a letter: "
        char = input(msg)


        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"
        else:
            wrong += 1
        print((" ".join(board)))
        print("\n".join(stages[0: wrong + 1]))
        if "__" not in board:
            print("You win! It was: ")
            print(" ".join(board))
            win = True
            break
    if not win:
         print("\n".join(stages[0:wrong]))
         print("You lose! It was {}.".format(word))

            
