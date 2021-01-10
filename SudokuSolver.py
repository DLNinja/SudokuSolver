sudoku = open('input.txt', 'r').readlines()
sudoku = [i.replace('\n', '').split(" ") for i in sudoku]
sudoku = [[int(x) for x in i] for i in sudoku]

def board(sudo):
    # print board
    print("-------------------------")
    for i in range(9):
        if i == 3 or i == 6:
            print("-------------------------")
        print("|", end=" ")
        for j in range(9):
            if j == 3 or j == 6:
                print("|", end=" ")
            print(sudo[i][j], end=" ")
        print("|")
    print("-------------------------")

def verify(sudo, i, j, nr):
    # verify if the value can be placed on position (i, j)

    a = i // 3
    b = j // 3

    # verifying line and column for the given value
    for k in range(9):
        if sudo[i][k] == nr and k != j:
            return False
    for k in range(9):
        if sudo[k][j] == nr and k != i:
            return False

    # verifying 'box' for given value
    for k in range(a * 3, a * 3 + 3):
        for f in range(b * 3, b * 3 + 3):
            if sudo[k][f] == nr and k != i and f != j:
                return False

    return True


def zero(sudo):
    # searching for a zero value
    for i in range(9):
        for j in range(9):
            if sudo[i][j] == 0:
                return i, j
    return False


def solution(sudo):
    # searches for zero on the board
    poz = zero(sudo)

    if not poz:
        # if there are no zeros we print the board
        board(sudo)
        return True
    else:
        # else, we continue with the zero value
        i, j = poz

    for nr in range(1, 10):
        if verify(sudo, i, j, nr):
            # finding a value to match the current spot
            sudo[i][j] = nr

            if solution(sudo):
                return True

            sudo[i][j] = 0

    return False


solution(sudoku)
