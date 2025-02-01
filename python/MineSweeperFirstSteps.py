import random as rand
#----- FUNCTIONS -----
def addMark(m,r,c,b):
    #if the space is blank, add that mine
    if b[r][c]==" ":
        b[r][c]=m   
        return True
    return False
#randomly addes the mine in
board=[
        ["+","1","2","3","4","5","6","7","8","9"],
        ["1"," "," "," "," "," "," "," "," "," "],
        ["2"," "," "," "," "," "," "," "," "," "],
        ["3"," "," "," "," "," "," "," "," "," "],
        ["4"," "," "," "," "," "," "," "," "," "],
        ["5"," "," "," "," "," "," "," "," "," "],
        ["6"," "," "," "," "," "," "," "," "," "],              #This is the board that the Mines and the numbers 
        ["7"," "," "," "," "," "," "," "," "," "],
        ["8"," "," "," "," "," "," "," "," "," "],
        ["9"," "," "," "," "," "," "," "," "," "]]
Mine="M"
numberList=[1,2,3,4,5]
def printBoard(b):                                              #todo explain print board in comments 
        for row in range(len(b)):                               #so this is saying for the row in range of the length of the board then 
            for col in range(len(b[row])):                      #for col in range of the length of the board print | else: make a space then if the row does not = the board length then print - 38 times
                if col !=(len(b[row])-1):
                      print(b[row][col],end=" | ")
                else:
                      print(b[row][col],end="\n")
            if row !=(len(b)-1):
                      print("-"*38)
        print()
for i in range (10):
    row = rand.randint(1,9)
    col = rand.randint(1,9)                                     #this is creating the Mine, row ,col and board and placing them randomly 1,9 times
    addMark(Mine,row,col,board)

printBoard(board)






