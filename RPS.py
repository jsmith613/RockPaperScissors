#1 = Rock
#2 = Paper
#3 = Scissors

from random import *

#Save file is made into a list, Each line is an item
f = open('Hard.txt','r')
readFile = []
lines = f.readlines()
for line in lines:
    line = line.rstrip('\n')
    readFile.append(line)
f.close()

f1 = open('Player.txt')
playerFile = []
for line in lines:
    line = line.rstrip('\n')
    playerFile.append(line)
f1.close()

aDict = {1:'Rock', 2:'Paper', 3:'Scissors'}

#used for Easy Mode
def getMode(memoryList):
    countrock = 0
    countscissors = 0
    countpaper = 0
    for x in memoryList:
        if x == 1:
            countrock = countrock + 1
        elif x == 2:
            countpaper = countpaper + 1
        else:
            countscissors = countscissors + 1
    modeList = [countrock,countscissors, countpaper]
    return(modeList.index(max(modeList)))



def predictEasy(mem):
        #mem is a list of previous guesses
        #tempguess equals random or most choosen option
        if len(mem) == 0:
            tempguess = randint(1,3)
        else:
            tempguess = getMode(mem) + 1
        return(tempguess)


def predictHard(last):
    #where prev is a string, first digit is users last input, second digit is cpu last input
    find = 'move:' + str(last)
    index = readFile.index(find)
    r = readFile[index + 1][2:]
    p = readFile[index + 2][2:]
    s = readFile[index + 3][2:]
    r = int(r)
    p = int(p)
    s = int(s)
    if r > p and r > s:
        return(1)
    elif p > r and p > s:
        return(2)
    elif s > r and s > p:
        return(3)
    elif r == p == s:
        return(randint(1,3))
    elif r == p:
        return(randint(1,2))
    elif p == s:
        return(randint(2,3))
    elif r == s:
        return(int(choice('13')))


def convert(inp):
        #input:user choice,  output:user choice as int
        #change string choice to int value
        if inp.lower() == 'rock' or inp.lower() == 'r':
            choice = 1
        elif inp.lower() == 'paper' or inp.lower() == 'p':
            choice = 2
        elif inp.lower() == 'Scissors' or inp.lower() == 's':
            choice = 3
        return(choice)

def aiMove(tg):
        #input: prediction,  output: chosen move
        #change prediction to AI throw
        if int(tg) == 3:
            guess = 1
        else:
            guess = int(tg) + 1
        return(guess)

#determining who wins
def detwin(c,g):
        #c is choice
        #g is guess
        #figure out who wins
        #winstatus determines if the AI wins

        winstatus = ""
        if c == g:
            winstatus = 'tie'
        elif c == 3 and g == 1:
            winstatus = 'lose'
        elif c == 1 and g ==3:
            winstatus = 'win'
        elif c < g:
            winstatus = 'lose'
        else:
            winstatus = 'win'
        return winstatus


def printResult(c,g,ws):
        #Add choice to list
        print("Your choice:" + str(aDict[c]))
        print("Computer Choice:" + str(aDict[g]))
        print('Result:' + str(ws))

#Changes readList to reflect results
def recordResult(l,c):
    find = "move:" + str(l)
    index = readFile.index(find)
    if c == 1:
        a = readFile[index + 1][2:]
        b = int(a) + 1
        readFile[index + 1] = 'r:' + str(b)
    elif c == 2:
        a = readFile[index+2][2:]
        b = int(a) + 1
        readFile[index + 2] = 'p:' + str(b)
    elif c == 3:
        a = readFile[index + 3][2:]
        b = int(a) + 1
        readFile[index + 3] = 's:' + str(b)

#Gets and Sets Rounds Played
def getRoundsPlayed():
    a = readFile[1][14:]
    b = int(a) + 1
    readFile[1] = 'Rounds Played:' + str(b)

def play():

    memory = []
    yourScore = 0
    computerScore = 0
    isDiffInputInvalid = True
    while (isDiffInputInvalid):

        difficulty = input("Choose a difficulty: Easy, Hard, Impossible!    ")
        #normalizing difficulty input value
        if difficulty.lower() == 'easy' or 'e':
            difficulty = 'easy'
        elif difficulty.lower() == 'hard' or 'h':
            difficulty = 'hard'
        elif difficulty.lower() == 'impossible' or 'impossible!' or 'i':
            difficulty = 'Impossible!'

        #checking if player had valid difficulty input
        if (difficulty != ('easy' or 'hard' or 'Impossible!')):
            print("That is not a valid input, try again")
            isDiffInputInvalid = True
        else:
            isDiffInputInvalid = False

    if difficulty.lower() == 'hard':
        gameString = readFile[0]
        readFile[0] = ('Opponents Played:' + str(int(gameString[17:]) + 1))
    last = 0

    while True:
        #reset values

        tempguess = 0
        choice = 0
        guess = 0
        isChoiceInputInvalid = True
        while(isChoiceInputInvalid):
            strchoice = input("Choose: Rock, Paper, Scissors, Quit    ")
            if strchoice.lower() == 'quit':
                return None
            elif strchoice.lower() == ('rock' or 'r'):
                strchoice = 'r'
            elif strchoice.lower() == ('paper' or 'p'):
                strchoice = 'p'
            elif strchoice.lower() == ('scissors' or 's'):
                strchoice = 's'
            if ((strchoice != 'r') and (strchoice != 'p') and (strchoice != 's')):
                print("That is not a valid input, try again")
                isChoiceInputInvalid = True
            else:
                isChoiceInputInvalid = False

        #Choose Difficulty and Predict user choice
        pre = ""
        if difficulty == 'easy':
            pre = predictEasy(memory)
        elif difficulty == 'hard':
            pre = predictHard(last)
        elif difficulty == 'Impossible!':
            pre = convert(strchoice)


        move = aiMove(pre)  #Convert Prediction to aI throw
        c = convert(strchoice)  #convert user input to user throw
        if difficulty == 'easy':
            memory.append(c)
        ws = detwin(c,move)    #Determine who wins
        if difficulty == 'hard':
            recordResult(last, c)
        last = str(c) + str(move)   #Used as argument for next round
        printResult(c,move,ws)      #prints results of round

        if ws == 'win':
            yourScore = yourScore + 1
        elif ws == 'lose':
            computerScore = computerScore + 1

        print("Your Score:" + str(yourScore))
        print("Computer Score:" + str(computerScore))
        print("")

        #Impossible Easter Egg
        if difficulty =='Impossible!':
            if computerScore == 3:
                ans = input("You actually cannot win....keep playing anyway?: Yes, No")
                if ans.lower() == 'no':
                    return None
            if computerScore == 10:
                print('Why do this to yourself??')
            if computerScore == 200:
                print("You are done now")
                return None

        #If Hard Mode, Keep track of round played
        if difficulty == 'hard':
            getRoundsPlayed()

        #write new results to medium.txt
        f1 = open('Hard.txt','w')
        for x in readFile:
            f1.write(x)
            f1.write('\n')
        f1.close()
play()