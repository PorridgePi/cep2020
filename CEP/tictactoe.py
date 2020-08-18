from time import sleep
def instruction():
    print("""
This is a Tic Tac Toe game.
Player 1 will be 'x' and player 2 will be 'o'.
The position to place on the board will be as follow:
    
        1|2|3
        -----
        4|5|6
        -----
        7|8|9
""")

def showBoard(state):
    print("\n")
    print("\t"+state[0],'|',state[1],'|',state[2],sep='')
    print('\t-----')
    print("\t"+state[3],'|',state[4],'|',state[5],sep='')
    print('\t-----')
    print("\t"+state[6],'|',state[7],'|',state[8],sep='')
    print('\n')
    
def update_state(player,position,state):
    if player==1:
        if state[position-1]==" ":
            state[position-1]='x'
        else:
            state[1000]='x'
    elif player==2:
        if state[position-1]==" ":
            state[position-1]='o'
        else:
            state[1000]='o'
    
def isWinner(b, l):
    return ((b[6] == l and b[7] == l and b[8] == l) or # across the top
            (b[3] == l and b[4] == l and b[5] == l) or # across the middle
            (b[0] == l and b[1] == l and b[2] == l) or # across the bottom
            (b[6] == l and b[3] == l and b[0] == l) or # down the left side
            (b[7] == l and b[4] == l and b[1] == l) or # down the middle
            (b[8] == l and b[5] == l and b[2] == l) or # down the right side
            (b[6] == l and b[4] == l and b[2] == l) or # diagonal
            (b[8] == l and b[4] == l and b[0] == l))   # diagonal

def getInput(player,state):
    p=input("Player "+str(player)+"'s move: ")
    while True:
        try:
            p = int(p)
            update_state(player,p,state)
            break
        except:
            p = input("Please enter a valid number from 1 to 9 which is not placed before.\nPlayer "+str(player)+"s move: ")
        
def game():
    instruction()
    winner=0
    state=[' ',' ',' ',
           ' ',' ',' ',
           ' ',' ',' ']
    while ' ' in state:
        getInput(1,state)
        showBoard(state)
        if isWinner(state,'x'):
            winner=1
            break
        if not ' ' in state:
            break
        getInput(2,state)
        showBoard(state)
        if isWinner(state,'o'):
            winner=2
            break
        if not ' ' in state:
            break
        
    if winner>0:
        print("Player",winner,"won!\n")
    else:
        print("Draw!\n")
        
def main():
    again="y"
    while again=="y":
        game()
        again=input("Do you want to play again? (y/n) ")
    print("\nBye!")
    sleep(2)
        
        
main()