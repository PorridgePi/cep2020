def printBoard(state):
    for i in state:
        for item in i:
            print(item, end='\t')
        print()


def move(state, direction):
    
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
