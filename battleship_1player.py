#### Make a game of battleship User vs Computer.
#### The board will be 9x9 squares.
#### The ship will take up two squares.

from random import randint

#define your board
board = []
alpha="### a  b  c  d  e  f  g  h  i"

for x in range(9):
    board.append(["O"] * 9)

def print_board(board): 
    num=0
    print alpha,"\n"
    for row in board:
        num += 1
        print num," ","  ".join(row)

#Opening text and first board
print "Let's play Battleship!\nRules: My ship is two coordinates long.\nYou will only be able to guess 9 positions, so make it count.\n\nHere's the board."
print_board(board)

#define ship's first coordinate
def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

#set ship's first coordinate
ship_col = random_col(board)
ship_row = random_row(board)

#define ship's second row coordinate in case of n-s ship
def random_row_2(board,ship_row):
    if ship_row <8 and ship_row > 0:
        row_2=ship_row+randint(-1,1)
        if row_2 == ship_row:
            row_2 = ship_row +1
            return row_2
        else:
            return row_2
    elif ship_row == 0:
        return ship_row + 1
    else:
        return ship_row - 1

#define ship's second col coordinate in case of e-w ship
def random_col_2(board,ship_col):
    if ship_col <8 and ship_col > 0:
        col_2=ship_col+randint(-1,1)
        if col_2 == ship_col:
            col_2 = ship_col +1
            return col_2
        else:
            return col_2
    elif ship_col == 0:
        return ship_col + 1
    else:
        return ship_col - 1

#set ship orientation and second coordinate
ship_orient=randint(1,2)
#if ship orientated n-s
if ship_orient == 1:
    ship_row_2=random_row_2(board,ship_row)
    ship_col_2=ship_col
#if ship orientated e-w
else:
    ship_col_2=random_col_2(board,ship_col)
    ship_row_2=ship_row

#start your turns
for turn in range(1,10):
    board_changed=False
    guess=raw_input("\nGuess #{}: ".format(turn))
    guess=guess.replace(" ","")
    #guess_col is checked with Error Check #2
    guess_col=int(ord((guess[0]).lower())-97)
    #Error Check #1: verify guess_row is int
    try:
        guess_row = int(guess[1:])-1
    except ValueError:
        print "\nOops, that's not even in the ocean."
    else:
        #Error Check #2: verify guess_col is alpha a-i; verify guess_row is int 1-9
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 8):
            print "\nOops, that's not even in the ocean."
        
        #check for hits
        elif guess_row == ship_row and guess_col == ship_col or \
           guess_row == ship_row_2 and guess_col == ship_col_2:
            board[guess_row][guess_col] = "!"
            hits=0
            for line in board:
                for square in line:
                    if square == "!":
                        hits = hits+1
            if hits == 2:
                print "You sank my battleship!\n"
                print_board(board)
                break
            elif hits == 1:
                print "You hit my battleship!"
                board_changed=True
        #Error Check #3: verify not repeat guess
        elif (board[guess_row][guess_col] == "X") or (board[guess_row][guess_col] == "!"):
            print "\nYou guessed that one already."
            
        else:
            print "\nYou missed my battleship!"
            board[guess_row][guess_col] = "X"
            board_changed=True
            
    if turn == 9:
        print "\nGame Over!"
        break
    else:
        if board_changed==True:
            print_board(board)
