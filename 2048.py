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
                if prevNum is not None:
                    newState[l].append(prevNum)
                prevNum = j[i]

            if (i + 1) == len(j) and prevNum is not None:
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


def string2matrix(string):
    result = [[], [], [], []]
    strs = string.replace('[', '').split('],')
    state = [map(int, s.replace(']', '').split(',')) for s in strs]
    for i in range(len(state)):
        for j in state[i]:
            result[i].append(j)
    return result


def test():
    state = [
        [2, 2, 2, 2],
        [4, 16, 4, 2],
        [2, 64, 64, 4],
        [1024, 1024, 64, 0]
    ]

    state = [[2, 2, 2, 2], [4, 16, 4, 2], [2, 64, 64, 4], [1024, 1024, 64, 0]]

    printBoard(state)
    printBoard(move(state, 'down'))


def main():
    string = input('Please enter an initial list to start the game.\n>>> ')
    state = string2matrix(string)
    print('\nThis is the original state:')
    printBoard(state)

    direction = input('Which direction do you want to move? [up, down, left, right]\n>>> ')
    newState = move(state, direction)

    print('\nThis is the new state:')
    printBoard(newState)


if __name__ == "__main__":
    main()
