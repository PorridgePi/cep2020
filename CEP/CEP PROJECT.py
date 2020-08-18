import random,sys,time,os,textwrap
def betterprint(text):
    #to do a scrolling print function instead of the line instantly popping in
    for i in text:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.01)
    sys.stdout.write('\n')
    
def checkchoice(question,array):
    #checks if the question is in the array, if its not it will keep on asking
    ask=input(question)
    while ask not in array:
        if ask.upper()=='EXIT':
            raise StopIteration
        else:
            ask=input('Invalid input. '+question)
    return ask
def instructionprint(text):
    for i in text:
        betterprint(i)
def main():
    stop=False
    instructions='''
This is a 5 in 1 game. You can choose from 5 different games to play:
1. 2 Player Tic Tac Toe
2. Hot or Cold
3. Rock Paper Scissors vs Computer
4. Bash the mole
5. Memory Game

To play the game, input the corresponding number to the game.
Input 'quit' to stop.
If u want to quit the game and come back to the main menu, input 'exit'.
Input 'instructions' to show this page.
'''
    
    betterprint(instructions)
    #check if the input is in this array
    games=['1','2','3','4','5']
    while stop!=True:
        game=input('Which game do you want to play?(Input \'instructions\' to show help): ')
        if  game.upper()=='QUIT':
            stop=True
        elif game.upper()=='INSTRUCTIONS':
            betterprint(instructions)
        #check if the input is 1-5
        elif game in games:
            game=int(game)
            if game==1:
                try:
                    tic_tac_toe()
                except StopIteration:
                    print('Game exited.')
                
            elif game==2:
                try:
                    hot_or_cold()
                except StopIteration:
                    print('Game exited.')
                
            elif game==3:
                try:
                    rock_paper_scissors()
                except StopIteration:
                    print('Game exited.')
                
            elif game==4:
                try:
                    bash_the_mole()
                except StopIteration:
                    print('Game exited.')
                
            elif game==5:
                try:
                    memory_game()
                except StopIteration:
                    print('Game exited.')
        
        else:
            betterprint('Invalid input.')

#defining the functions only related to the game inside the game function
def tic_tac_toe():
    def showBoard(state):
        #show the current tictactoe board
        print(state[0],'|',state[1],'|',state[2],sep='')
        print('-----')
        print(state[3],'|',state[4],'|',state[5],sep='')
        print('-----')
        print(state[6],'|',state[7],'|',state[8],sep='')
        
    def ask_player(player):
        answer=input('PUT IN YOUR MOVE PLAYER '+player+'!: ')
        ints=['1','2','3',
              '4','5','6',
              '7','8','9']
        if answer.upper()=='HELP':
            betterprint(instruction)
            return ask_player(player)
        #check if input is a valid number
        elif answer in ints:
            answer=int(answer)
            return answer
        elif answer.upper()=='EXIT':
            raise StopIteration
        else:
            return ask_player(player)

    def update_state(player,position,state):
        if player=='1':
            state[position-1] = 'x'
        elif player=='2':
            state[position-1] = 'o'  

    def check_state(player,state):
        position = ask_player(player)
        #to prevent overriding of the previous person's answer
        while state[position-1] != ' ':
            betterprint('This spot has already been taken up.')
            position = ask_player(player) #will reccur until player gives a non-conflicting answer
        update_state(player,position,state)

    def endgame(xo):
        condition=False
        #possible win conditions when the board is not full
        for i in range(3):
            if state[i*3]==xo and state[i*3+1]==xo and state[i*3+2]==xo:
                condition=True
            elif state[i]==xo and state[3+i]==xo and state[6+i]==xo:
                condition=True
        if state[0]==xo and state[4]==xo and state[8]==xo:
            condition=True
        elif state[2]==xo and state[4]==xo and state[6]==xo:
            condition=True
    
        if condition==True:
            winner(xo)
            return True
        #entire board is full
        if ' ' not in state:
            winner('yes')
            return True
        
    def winner(xo):
        if xo=='x':
            betterprint('Player 1 wins the game!')
        elif xo=='o':
            betterprint('Player 2 wins the game!')
        else:
            betterprint('Draw!')
    #defining variables for the game
    instruction='''
This is a Tic Tac Toe game.
Player 1 will be 'x' and player 2 will be 'o'.
To play, type the number corresponding to the
position in the board below:
1|2|3
-----
4|5|6
-----
7|8|9
Input 'help' to show this screen again.
Input 'exit'Test cases
'''
    betterprint(instruction)
    state = [' ',' ',' ',
             ' ',' ',' ',
             ' ',' ',' ']
    while not endgame('x') or not endgame('o'): 
        check_state('1',state)
        showBoard(state)
        if endgame('x') or endgame('o'):
            break
        check_state('2',state)
        showBoard(state)

def hot_or_cold():
    instructionprint(textwrap.wrap('This is a Hot or Cold guessing game. The program will generate a random number from 1-99. You will need to guess the number. If your guess is closer to the number, the program will output a temperature depending on the closeness of your guess to the number. The higher the temperature, the closer the guess. Input \'exit\' to go back to main menu.'))
    answer=random.randint(1,99)
    #generating a number list to check with the input
    numbers=[]
    for i in range(1,100):
        numbers.append(str(i))
    guess=int(checkchoice('Guess a number from 1-99: ',numbers))
    tries=1
    start=True
    #checking if the guess is close to the answer
    while start==True:
        diff=abs(guess-answer)
        if diff>60:
            betterprint('Icecold')

        elif diff>30:
            betterprint('Cold')
            
        elif diff>20:
            betterprint('Cool')
            
        elif diff>10:
            betterprint('Warm')
            
        elif diff>5:
            betterprint('Hot')

        elif diff>0:
            betterprint('Boiling')
            
        elif diff==0:
            #for proper grammar
            if tries==1:
                singular='try.'
            else:
                singular='tries.'
            betterprint('Yay! You have guessed the number in '+str(tries)+' '+str(singular))
            start=False
            continue
        tries+=1
        guess=int(checkchoice('Guess a number from 1-99: ',numbers))
        
def rock_paper_scissors():
    def win(choice,computer):
        global playerscore
        global computerscore
        states=['rock','paper','scissors']
        player=states.index(choice)
        if player==computer:
            betterprint('Draw. You both chose '+states[player])
        #checking win conditions
        elif player>computer:
            if player==2 and computer==0:
                computerscore+=1
                betterprint('You lose! You chose '+states[player]+'. Computer chose '+ states[computer])
            else:
                playerscore+=1
                betterprint('You win! You chose '+states[player]+'. Computer chose '+ states[computer])
        elif computer>player:
            if computer==2 and player==0:
                playerscore+=1
                betterprint('You win! You chose '+states[player]+'. Computer chose '+ states[computer])
            else:
                computerscore+=1
                betterprint('You lose! You chose '+states[player]+'. Computer chose '+ states[computer])
                

    instructionprint(textwrap.wrap('This is a rock paper scissors game played against the computer. The player will choose either rock, paper or scissors and the computer will randomise one of the 3. When either the player or the computer has 3 wins, the game ends. Input \'exit\' to go back to main menu.'))
    global playerscore
    global computerscore
    playerscore=0
    computerscore=0
    start=True
    while start==True:
        randomiser=random.randint(0,2)
        answer=checkchoice('Your choice(rock, paper or scissors): ',['rock','paper','scissors'])
        win(answer,randomiser)
        if playerscore==3:
            betterprint('You win! You have 3 points, computer has '+str(computerscore)+' points!')
            start=False
        elif computerscore==3:
            betterprint('You lose! You have '+str(playerscore)+' points, computer has 3 points!')
            start=False

def bash_the_mole():
    def ask_player(player=""):
        global tries
        answer=input('WHICH HOLE DO YOU WANT TO BASH{}?: '.format(player))
        ints=['1','2','3',
              '4','5','6',
              '7','8','9']
        if answer.upper()=='HELP':
            betterprint(instruction)
            return ask_player()
        elif answer.upper()=='SCORE':
            #show score
            betterprint('Your score is '+str(score))
            return ask_player()
        elif answer.upper()=='TRIES':
            #show tries
            betterprint('You have done '+str(tries)+' tries.')
            return ask_player()
        elif answer.upper()=='EXIT':
            raise StopIteration
        elif answer in ints:
            answer=int(answer)
            tries+=1
            return answer
        else:
            return ask_player()
    
    def bash_mole():
        moles=[random.randint(1,9),random.randint(1,9)]
        player=ask_player()
        array=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
        def check_mole(mole):
            if moles[mole]==player:
                betterprint('You bashed mole {}! It appeared in hole {}.'.format((mole+1),str(moles[mole])))
                array[moles[abs(mole-1)]-1]=str(1+abs(mole-1))
                array[player-1]='§'
                #printing out the positions if the mole got bashed
                for i in range(3):
                    i*=3
                    thing=array[i],'|',array[i+1],'|',array[i+2]
                    betterprint(thing)
                    if i!=6:
                        betterprint('-----')
                return True
        #both moles appeared in the same hole and were bashed
        if moles[0]==moles[1] and moles[1]==player:
            betterprint('You bashed both the moles! They appeared in hole {}.'.format(str(player)))
            array[player-1]='§'
            for i in range(3):
                i*=3
                thing=array[i],'|',array[i+1],'|',array[i+2]
                betterprint(thing)
                if i!=6:
                    betterprint('-----')
            return 1
        #one mole was bashed
        elif check_mole(0):
            return 1

        elif check_mole(1):
            return 1
        #no moles were bashed
        else:
            betterprint('You missed the mole! Mole 1 appeared in hole {} and Mole 2 appeared in hole {}.'.format(moles[0],moles[1]))
            if moles[0]!=moles[1]:
                array[moles[0]-1]='1'
                array[moles[1]-1]='2'
            else:
                #both moles in the same spot
                array[moles[0]-1]='∞'
            array[player-1]='x'
            #printing out the positions for miss the mole
            for i in range(3):
                i*=3
                thing=array[i],'|',array[i+1],'|',array[i+2]
                betterprint(thing)
                if i!=6:
                    betterprint('-----')
            return 0       
               
    instruction='''
This is a bash the mole game. Two moles will randomly
appear in one of the 9 holes.
1|2|3
-----
4|5|6
-----
7|8|9
You must guess correctly the position of the hole that a mole
will appear in to bash it. You will gain one point if you bash
it. 5 points and you will win. After you make a guess, a
table will show up showing you where you bashed and where the
moles were. 1 is the location of the first mole. 2 is the
location of the second mole. x is the location of the bash
if you did not hit any moles. If both moles appeared in the same
hole but you did not bash them there will be a ∞ at the hole
§ will show up if you succesfully
bashed one of the moles. Type 'help' to show this page again.
Type 'score' to see your score. Type 'tries' to see how many tries
you have done so far. Input 'exit' to go back to main menu.
'''
    
    score=0
    global tries
    tries=0
    betterprint(instruction)
    run=True    
    while run==True:
        score+=bash_mole()
        if score==5:
            run=False
            betterprint('You tried '+str(tries)+' times and bashed the mole 5 times! Good job! He definitely won\'t bother you again!')
            
def memory_game():
    #asks the player how many numbers they want to memorise and how long they want to be given
    def ask_player():
        number=input('How many numbers do you want to memorise?: ')
        #checks if it is a integer
        if number.isdecimal():
            number=int(number)
        elif number.upper()=='EXIT':
            raise StopIteration
        else:
            while not number.isdecimal():
                number=input('Please input a number. How many numbers do you want to memorise?: ')
            number=int(number)
        time=input('How long do you want to be given to memorise each number?(seconds): ')
        if time.isdecimal():
            time=int(time)
        elif time.upper()=='EXIT':
            raise StopIteration
        else:
            while not time.isdecimal():
                time=input('Please input a number. How long do you want to be given to memorise each number?(seconds): ')
            time=int(time)
        return number,time
    #generates a list of numbers according to how many the player wants
    def number_generation():
        numbers=[]
        for i in range(number):
            thing=random.randint(1,99)
            betterprint(str(thing))
            time.sleep(wait)
            #makes the screen scroll up so that the previous number cannot be seen
            print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
            #adds the numbers to a array to check
            numbers.append(thing)
        return numbers

    description=textwrap.wrap("This is a memory game. The player will input how many numbers they want to memorise and the time they will be given to look at each number. Numbers from 1-99 will be randomised and shown on the screen and disappear after the given time. The player must remember the numbers and say them in the correct order. Input 'exit' to go back to main menu.")

    run=True
    instructionprint(description)
    number,wait=ask_player()
    numbers=number_generation()
    corrects=0
    wrongs=0
    #playerguesses each number
    for i in range(len(numbers)):
        playerguess=input('Number {}: '.format(i+1))
        #checks if its a valid guess
        if playerguess.isdecimal():
            playerguess=int(playerguess)
        elif playerguess.upper()=='EXIT':
            raise StopIteration
        else:
            while not playerguess.isdecimal():
                playerguess=input('Please input a number. Number {}: '.format(i+1))
            playerguess=int(playerguess)
        #checks if it corresponds to the generated number
        if playerguess==numbers[i]:
            betterprint('Correct.')
            corrects+=1
        else:
            betterprint('Wrong. The number was {}.'.format(numbers[i]))
            wrongs+=1
    #ouput 
    betterprint('You got {} numbers correct.'.format(corrects))
    betterprint('You got {} numbers wrong.'.format(wrongs))
    betterprint('The numbers were: ')
    count=1
    for i in numbers:
        betterprint('{}. {}'.format(str(count),str(i)))
        count+=1
    betterprint('Great job! You got {} numbers correct!'.format(corrects))

main()
