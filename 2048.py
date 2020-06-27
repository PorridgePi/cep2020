def transpose(state):
    newState = []
    for i in range(len(state[0])):
        newState.append([])
        for j in range(len(state)):
            newState[i].append(state[j][i])
    return newState


def reverse(state):
    newState = []
    for i in range(len(state)):
        newState.append([])
        for j in range(len(state[0])):
            newState[i].append(state[i][len(state[0])-j-1])
    return newState


def moveLeft(state):
    newState = [[], [], [], []]
    for l in range(len(state)):
        j = [a for a in state[l] if a != 0]
        prevNum = None
        for i in range(len(j)):
            if j[i] == prevNum:
                newState[l].append(j[i]*2)
                prevNum = None
            else:
                if prevNum != None:
                    newState[l].append(prevNum)
                prevNum = j[i]

            if (i + 1) == len(j) and prevNum != None:
                newState[l].append(prevNum)

        for i in range(4):
            while len(newState[l]) < 4:
                newState[l].append(0)
    return newState


def move(state, direction):
    if direction == 'left':
        return moveLeft(state)
    elif direction == 'right':
        return reverse(moveLeft(reverse(state)))
    elif direction == 'up':
        return transpose(moveLeft(transpose(state)))
    elif direction == 'down':
        return transpose(reverse(moveLeft(reverse(transpose(state)))))


def printBoard(state):
    for i in state:
        for item in i:
            print(item, end='\t')
        print()
    print()


def main():
    pass


state = [
    [2, 2, 2, 2],
    [4, 16, 4, 2],
    [2, 64, 64, 4],
    [1024, 1024, 64, 0]
]

printBoard(state)
printBoard(move(state, 'down'))
