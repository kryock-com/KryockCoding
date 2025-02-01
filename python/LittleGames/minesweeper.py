"""import random as rand

#----- Varaables -----
numOfFlags=10


#----- FUNCTIONS -----

#randomly addes the mine in
def addMark(m,r,c,b):
    #if the space is blank, add that mine
    if b[r][c]==" ":
        b[r][c]=m
        return True
    return False

board=[
        ["+","A","B","C","D","E","F","G","H","I"],
        ["1"," "," "," "," "," "," "," "," "," "],
        ["2"," "," "," "," "," "," "," "," "," "],
        ["3"," "," "," "," "," "," "," "," "," "],
        ["4"," "," "," "," "," "," "," "," "," "],
        ["5"," "," "," "," "," "," "," "," "," "],
        ["6"," "," "," "," "," "," "," "," "," "],
        ["7"," "," "," "," "," "," "," "," "," "],
        ["8"," "," "," "," "," "," "," "," "," "],
        ["9"," "," "," "," "," "," "," "," "," "]]
Mine="M"
numberList=[1,2,3,4,5]
def printBoard(b):
        for row in range(len(b)):
            for col in range(len(b[row])):
                if col !=(len(b[row])-1):
                      print(b[row][col],end=" | ")
                else:
                      print(b[row][col],end="\n")
            if row !=(len(b)-1):
                      print("-"*38)
        print()

        for i in range (10):
            n=9
            row = rand.randint(1,9)
            col = rand.randint(1,9)
            addMark(Mine,row,col,board)
            # N -->  North        (row-1, col)
            if row > 0:
                #Mine(row-1, col)
                #addMark("O",row-1,col,board)
                if board[row-1][col] in [" ","A","B","C","D","E","F","G","H","I","M"]:
                    board[row-1][col]=str(1)
                else:
                    board[row-1][col]=str(int(board[row-1][col])+1)
            # S -->  South        (row+1, col)           
            if row < n-1:
                #Mine(row+1, col)
                #addMark("O",row+1,col,board)
                if board[row+1][col] in [" ","A","B","C","D","E","F","G","H","I","M"]:
                    board[row+1][col]=str(1)
                else:
                    board[row+1][col]=str(int(board[row+1][col])+1)

            # W -->  West         (row, col-1)          
            if col > 0:
                #Mine(row, col-1)
                #addMark("O",row,col-1,board)
                if board[row][col-1] in [" ","A","B","C","D","E","F","G","H","I","M"]:
                    board[row][col-1]=str(1)
                else:
                    board[row][col-1]=str(int(board[row][col-1])+1)

            # E -->  East         (row, col+1)     
            if col < n-1:
                #Mine(row, col+1)
               # addMark("O",row,col+1,board)
                if board[row][col+1] in [" ","A","B","C","D","E","F","G","H","I","M","+"]:
                    board[row][col+1]=str(1)
                else:
                    board[row][col+1]=str(int(board[row][col+1])+1)    

            # N.W--> North-Eats   (row-1, col-1)
            if row > 0 and col > 0:
                #Mine(row-1, col-1)
                #addMark("O",row-1,col-1,board)
                if board[row-1][col] in [" ","A","B","C","D","E","F","G","H","I","M"]:
                    board[row-1][col]=str(1)
                else:
                    board[row-1][col]=str(int(board[row-1][col])+1)

            # N.W--> North-West   (row-1, col-1) 
            if row > 0 and col < n-1:
                #Mine(row-1, col+1)
              #  addMark("O",row-1,col+1,board)

            
            # S.W--> South-West   (row+1, col-1)  
            #if row < n-1 and col > 0:
                #Mine(row+1, col-1)
               # addMark("O",row+1,col-1,board)

            # S.E--> South-East   (row+1, col+1)             
            #if row < n-1 and col < n-1:
                #Mine(row+1, col+1)
              #  addMark("O",row+1,col+1,board)

        #print(col)
        #print(row)

             newboard=[]
    #secure_random = rand.SystemRandom()
    #res = [int(sub.split('.')[1]) for sub in numberList]





#for when you need to print flags
#print("Flags- {}".format(int(numOfFlags)))

#----- RUNNING CODE -----

#https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20
def title():
    print(' ▄▄       ▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄        ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ ')
    print('▐░░▌     ▐░░▌▐░░░░░░░░░░░▌▐░░▌      ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌')
    print('▐░▌░▌   ▐░▐░▌ ▀▀▀▀█░█▀▀▀▀ ▐░▌░▌     ▐░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌')
    print('▐░▌▐░▌ ▐░▌▐░▌     ▐░▌     ▐░▌▐░▌    ▐░▌▐░▌          ▐░▌          ▐░▌       ▐░▌▐░▌          ▐░▌          ▐░▌       ▐░▌▐░▌          ▐░▌       ▐░▌')
    print('▐░▌ ▐░▐░▌ ▐░▌     ▐░▌     ▐░▌ ▐░▌   ▐░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌   ▄   ▐░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌')
    print('▐░▌  ▐░▌  ▐░▌     ▐░▌     ▐░▌  ▐░▌  ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌  ▐░▌  ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌')
    print('▐░▌   ▀   ▐░▌     ▐░▌     ▐░▌   ▐░▌ ▐░▌▐░█▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀█░▌▐░▌ ▐░▌░▌ ▐░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀█░█▀▀ ')
    print('▐░▌       ▐░▌     ▐░▌     ▐░▌    ▐░▌▐░▌▐░▌                    ▐░▌▐░▌▐░▌ ▐░▌▐░▌▐░▌          ▐░▌          ▐░▌          ▐░▌          ▐░▌     ▐░▌  ')
    print('▐░▌       ▐░▌ ▄▄▄▄█░█▄▄▄▄ ▐░▌     ▐░▐░▌▐░█▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄█░▌▐░▌░▌   ▐░▐░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌          ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌      ▐░▌ ')
    print('▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░▌      ▐░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░▌     ▐░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌          ▐░░░░░░░░░░░▌▐░▌       ▐░▌')
    print(' ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀        ▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀       ▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀            ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀ ')
title()

howToPlay=input("Do you want to see the instructions to play?- ").lower()
if howToPlay == "yes":
    print("\nThe numbers on the board represent how many bombs are adjacent to a",
    "\nsquare. For example, if a square has a '3' on it, then there are 3 bombs",
    "\nnext to that square. The bombs could be above, below, right left, or",
    "\ndiagonal to the square. Avoid all the bombs and expose all the empty",
    "\nspaces to win Minesweeper.\n"
    "\The 0's on the board show there are no bomb around that square.")
gamemode=input("Are you ready?- ").lower()
while gamemode != "yes":
    gamemode=input("Are you ready?- ").lower()


#flag emoji https://emojipedia.org/triangular-flag/
#:triangular_flag_on_post:
flags=":triangular_flag_on_post:"

print(flags)

while Mine!="Q":
    correctInput = False
    #while not correctInput:
    print()
    printBoard(board)
    #Remeber that you need to do action if statments do if action == ui flags then create a if statment
    #do this with flag, col, row
    row=int(input("Which row? "))
    col=int(input("Which col? "))
    #action=input("What action would you like to do?").lower()
    #if action=="flag":
        #addMark(Flags,row,col,board)
        #print updated board make this into a class 
    #if action=="step":
        #this is where the algo for checking for mine goes

    if not((0<=row<=9) and (0<=col<=9)):
        print("The row and column are not correct")
    #try to add a mark, and if you do, this is true.....
    elif board[row][col] =="M":
        print("Game Over")
        break               
    elif not(addMark(Mine,row,col,board)):
        print("That space was already taken")
    
    else:
        correctInput=True







This will help with the algoritm to check 
Cell-->Current Cell (row, col) 
        N -->  North        (row-1, col) 
        S -->  South        (row+1, col) 
        E -->  East         (row, col+1) 
        W -->  West            (row, col-1) 
        N.E--> North-East   (row-1, col+1) 
        N.W--> North-West   (row-1, col-1) 
        S.E--> South-East   (row+1, col+1) 
        S.W--> South-West   (row+1, col-1)
"""

import random as rand

# Constants
BOARD_SIZE = 9
MINE = "M"
FLAG = "F"
EMPTY = " "

# Initialize Board
def create_board(size):
    board = [[EMPTY for _ in range(size)] for _ in range(size)]
    return board

# Add Mines
def place_mines(board, num_mines):
    for _ in range(num_mines):
        while True:
            row, col = rand.randint(0, BOARD_SIZE - 1), rand.randint(0, BOARD_SIZE - 1)
            if board[row][col] == EMPTY:
                board[row][col] = MINE
                break

# Update Numbers Around Mines
def update_numbers(board):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] == MINE:
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < BOARD_SIZE and 0 <= nc < BOARD_SIZE and board[nr][nc] != MINE:
                        if board[nr][nc] == EMPTY:
                            board[nr][nc] = "1"
                        else:
                            board[nr][nc] = str(int(board[nr][nc]) + 1)

# Print Board
def print_board(board, revealed, flags):
    print("   " + " ".join([chr(65 + i) for i in range(BOARD_SIZE)]))
    for i, row in enumerate(board):
        row_display = []
        for j, cell in enumerate(row):
            if (i, j) in flags:
                row_display.append(FLAG)
            elif (i, j) in revealed:
                row_display.append(cell)
            else:
                row_display.append("#")
        print(f"{i + 1:2} " + " ".join(row_display))

# Reveal Cell
def reveal(board, revealed, row, col):
    if (row, col) in revealed:
        return
    revealed.add((row, col))
    if board[row][col] == EMPTY:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        for dr, dc in directions:
            nr, nc = row + dr, col + dc
            if 0 <= nr < BOARD_SIZE and 0 <= nc < BOARD_SIZE:
                reveal(board, revealed, nr, nc)

# Main Game Loop
def play_game():
    board = create_board(BOARD_SIZE)
    place_mines(board, 10)
    update_numbers(board)
    
    revealed = set()
    flags = set()

    #https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20
    def title():
        print(' ▄▄       ▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄        ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ ')
        print('▐░░▌     ▐░░▌▐░░░░░░░░░░░▌▐░░▌      ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌')
        print('▐░▌░▌   ▐░▐░▌ ▀▀▀▀█░█▀▀▀▀ ▐░▌░▌     ▐░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌')
        print('▐░▌▐░▌ ▐░▌▐░▌     ▐░▌     ▐░▌▐░▌    ▐░▌▐░▌          ▐░▌          ▐░▌       ▐░▌▐░▌          ▐░▌          ▐░▌       ▐░▌▐░▌          ▐░▌       ▐░▌')
        print('▐░▌ ▐░▐░▌ ▐░▌     ▐░▌     ▐░▌ ▐░▌   ▐░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌   ▄   ▐░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌')
        print('▐░▌  ▐░▌  ▐░▌     ▐░▌     ▐░▌  ▐░▌  ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌  ▐░▌  ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌')
        print('▐░▌   ▀   ▐░▌     ▐░▌     ▐░▌   ▐░▌ ▐░▌▐░█▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀█░▌▐░▌ ▐░▌░▌ ▐░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀█░█▀▀ ')
        print('▐░▌       ▐░▌     ▐░▌     ▐░▌    ▐░▌▐░▌▐░▌                    ▐░▌▐░▌▐░▌ ▐░▌▐░▌▐░▌          ▐░▌          ▐░▌          ▐░▌          ▐░▌     ▐░▌  ')
        print('▐░▌       ▐░▌ ▄▄▄▄█░█▄▄▄▄ ▐░▌     ▐░▐░▌▐░█▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄█░▌▐░▌░▌   ▐░▐░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌          ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌      ▐░▌ ')
        print('▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░▌      ▐░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░▌     ▐░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌          ▐░░░░░░░░░░░▌▐░▌       ▐░▌')
        print(' ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀        ▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀       ▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀            ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀ ')
    title()
    
    while True:
        print_board(board, revealed, flags)
        action = input("Enter action (reveal/flag) and cell (e.g., reveal B3): ").strip().lower()
        if len(action.split()) != 2:
            print("Invalid input format.")
            continue
        act, cell = action.split()
        if len(cell) < 2 or not cell[1:].isdigit():
            print("Invalid cell format.")
            continue
        col = ord(cell[0].upper()) - 65
        row = int(cell[1:]) - 1
        if not (0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE):
            print("Cell out of bounds.")
            continue
        
        if act == "reveal":
            if board[row][col] == MINE:
                print("Game Over!")
                break
            reveal(board, revealed, row, col)
            if len(revealed) == BOARD_SIZE * BOARD_SIZE - 10:
                print("You win!")
                break
        elif act == "flag":
            if (row, col) in flags:
                flags.remove((row, col))
            else:
                flags.add((row, col))
        else:
            print("Invalid action.")

play_game()
