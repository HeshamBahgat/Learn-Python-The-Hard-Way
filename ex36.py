# Tic Tac Toe

import random




def drawboard(board):
    # This function prints out the board that is was passed.
    # board is a list of 10 strings representing the board (ignore index 0)
    print("  |    |")
    print(" " + board[7] + board[8] + board[9])
    print("  |    |")
    print("------------------------")
    print("  |    |")
    print(" " + board[4] + board[5] + board[6])
    print("  |    |")
    print("------------------------")
    print("  |    |")
    print(" " + board[1] + board[2] + board[3])
    print("  |    |")
    print("------------------------")




def inputplayerletter():
    # Lets make the palyer type - which letter they want to be.
    # Return a list with the players letter as the first item, and the computer's letter as the secound.
    letter = ""
    while not (letter == "X" or letter == "O"):
        print("Do you want to be X or O?")
        letter = input().upper()
    # the first element in the list is the player's tag, the second is the computer's letter
    if letter == "X":
        return ["X", "O"]
    else:
        return ["O", "X"]

def whogoesfirst():
    # Randomly choose the player who goes first.
    if random.randint(0, 1) == 0:
        return "computer"
    else:
        return "player"


def playagain():
    # this function returns True if the player wants to play agian, otherwise it returns False.
    print("Do you want to play again? (yes or no)")
    return input().lower().startswith("y")


def makemove(board, letter, move):
    board[move] = letter


def iswinner(bo, le):
    print(le)
    print(bo)

    # Given a board and player's letter, this function returns True if that player won.
    # We use bo instead of board and le instead of letter so we dont have to type as much.
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or
            (bo[4] == le and bo[5] == le and bo[6] == le) or
            (bo[1] == le and bo[2] == le and bo[3] == le) or
            (bo[3] == le and bo[6] == le and bo[9] == le) or
            (bo[2] == le and bo[5] == le and bo[8] == le) or
            (bo[1] == le and bo[4] == le and bo[7] == le) or
            (bo[1] == le and bo[5] == le and bo[9] == le) or
            (bo[3] == le and bo[5] == le and bo[7] == le))




def getboardcopy(board):
    # make a duplicate of the board list and return it the duplicate.
    dupeboard = []
    for i in board:
        dupeboard.append(i)
    return dupeboard



def isspacefree(board, move):
    # return true if the passed move is free on the passed board.
    return board[move] == " "


def getplayermove(board):
    # let the player type in ther move
    move = " "
    while move not in ("1 2 3 4 5 6 7 8 9".split() or isspacefree(board, int(move))):
        print("What is your next move? (1 - 9)")
        move = input()
    return int(move)



def chooserandommovefromlist(board, moveslist):
    # return a valid move from the passed list on the passed board
    # return none if there is no valid move.
    possiblemoves = []
    for i in moveslist:
        if isspacefree(board, i):
            possiblemoves.append(i)
    if len(possiblemoves) != 0:
        return random.choice(possiblemoves)
    else:
        return None


def getcomputermove(board, computerletter):
    # given a board and the computer's letter, determine where to move and return that move.
    if computerletter == "X":
        playerletter = "O"
    else:
        playerletter = "X"
    # Here is our algorithm for our Tic Tac Toe AI:
    # First, check if we can win in the next move
    for i in range(1, 10):
        copy = getboardcopy(board)
        if isspacefree(copy, i):
            makemove(copy, computerletter, i)
            if iswinner(copy, computerletter):
                return i
    # check if the player could win on his next move, and black them.
    for i in range(1, 10):
        copy = getboardcopy(board)
        if isspacefree(copy, i):
            makemove(copy, playerletter, i)
            if iswinner(copy, playerletter):
                return i
    # Try to take one of the corners, if they are free.
    move = chooserandommovefromlist(board, [1, 3, 7, 9])
    if move != None:
        return move
    # Try to take the center, if it is free.
    if isspacefree(board, 5):
        return 5

    # Move on one of the sides.
    return chooserandommovefromlist(board, [2, 4, 6, 8])



def isboardfull(board):
    # Return True if every space on the board has been taken. otherwise return False
    for i in range(1, 10):
        if isspacefree(board, i):
            return False
    return True


print("Welcome to Tic Tac Toe")

while True:
    # Reset the board
    theboard = [' '] * 10
    playerletter, computerletter = inputplayerletter()
    turn = whogoesfirst()
    print(" The " + turn + " Will go first.")
    gameisplaying = True

    while gameisplaying:
        if turn == "player":
            # Player's turn
            drawboard(theboard)
            move = getplayermove(theboard)
            makemove(theboard, playerletter, move)
            print(theboard)

            if iswinner(theboard, playerletter):
                drawboard(theboard)
                print("Hooray! You have won the game!")
                gameisplaying = False
            else:
                if isboardfull(theboard):
                    drawboard(theboard)
                    print("the game is a tie!")
                    break
                else:
                    turn = "computer"
        else:
            # computer's turn
            move = getcomputermove(theboard, computerletter)
            makemove(theboard, computerletter, move)
            if iswinner(theboard, computerletter):
                drawboard(theboard)
                print("The computeer has beaten you! You lose.")
                gameisplaying = False
            else:
                if isboardfull(theboard):
                    drawboard(theboard)
                    print('The game is a tie!')
                    break
                else:
                    turn = "player"
    if not playagain():
        break