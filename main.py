import os    
import time    
    
board = ['0','1','2','3','4','5','6','7','8','9']    
player = 1    
   
########win Flags##########    
Win = 1    
Draw = -1    
Running = 0    
Stop = 1    
###########################    
Game = Running    
Mark = 'X'    
   
#This Function Draws Game Board    
def DrawBoard():    
    print(" %c | %c | %c " % (board[1],board[2],board[3]))    
    print("___|___|___")    
    print(" %c | %c | %c " % (board[4],board[5],board[6]))    
    print("___|___|___")    
    print(" %c | %c | %c " % (board[7],board[8],board[9]))    
    print("   |   |   ")    
   
#This Function Checks position is empty or not    
def CheckPosition(x):    
    if(board[x]!="X"and board[x]!="O"):    
        return True    
    else:    
        return False    
   
#This Function Checks player has won or not    
def CheckWin():    
    global Game    
    #Horizontal winning condition    
    if(board[1] == board[2] and board[2] == board[3] and board[1] != ' '):    
        Game = Win    
    elif(board[4] == board[5] and board[5] == board[6] and board[4] != ' '):    
        Game = Win    
    elif(board[7] == board[8] and board[8] == board[9] and board[7] != ' '):    
        Game = Win    
    #Vertical Winning Condition    
    elif(board[1] == board[4] and board[4] == board[7] and board[1] != ' '):    
        Game = Win    
    elif(board[2] == board[5] and board[5] == board[8] and board[2] != ' '):    
        Game = Win    
    elif(board[3] == board[6] and board[6] == board[9] and board[3] != ' '):    
        Game=Win    
    #Diagonal Winning Condition    
    elif(board[1] == board[5] and board[5] == board[9] and board[5] != ' '):    
        Game = Win    
    elif(board[3] == board[5] and board[5] == board[7] and board[5] != ' '):    
        Game=Win    
    #Match Tie or Draw Condition    
    elif((board[1]=='X' or board[1]=='O') and (board[2]=='X' or board[2]=='O') and (board[3]=='X' or board[3]=='O') and (board[4]=='X' or board[4]=='O') and (board[5]=='X' or board[5]=='O') and (board[6]=='X' or board[6]=='O') and (board[7]=='X' or board[7]=='O') and (board[8]=='X' or board[8]=='O') and (board[9]=='X' or board[9]=='O')):
        Game=Draw    
    else:            
        Game=Running    
        
while(Game == Running):    
    os.system('cls')    
    DrawBoard()    
    if(player % 2 != 0):    
        print("Ruch X")    
        Mark = 'X'    
    else:    
        print("Ruch O")    
        Mark = 'O'    
    choice = int(input("Gdzie chcesz zaznaczyć?: "))    
    if(CheckPosition(choice)):    
        board[choice] = Mark    
        player+=1    
        CheckWin()    
    
os.system('cls')    
DrawBoard()    
if(Game==Draw):    
    print("Remis!")    
elif(Game==Win):    
    player-=1    
    if(player%2!=0):    
        print("Wygrywa X!")    
    else:    
        print("Wygrywa O!") 