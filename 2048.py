
def transpose(matrix):
    result = []
    for i in range(len(matrix[0])):
        new.append([])
        for j in range(len(matrix)):
            new[i].append(matrix[j][i])
    return result

def printBoard(state):
    for i in state:
        for item in i:
            print(item, end='\t')
        print()


def move(state, direction):
    if direction == 'up':

    for i in range(4):

    pass


def main():
    pass


state = [
    [2, 0, 0, 2],
    [4, 16, 8, 2],
    [2, 64, 32, 4],
    [1024, 1024, 64, 0]
]

printBoard(state)
