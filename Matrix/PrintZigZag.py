A = [[1, 2, 3, 4],
     [2, 3, 4, 5],
     [8, 6, 5, 4],
     [0, 9, 8, 7]]
order = 1


def printZigZag(A, order):
    for i in range(len(A[0])):
        if order > 0:
            for j in range(len(A[0])):
                print(A[i][j])
        else:
            for j in range(len(A[0]) - 1, -1, -1):
                print(A[i][j])
        order *= -1


printZigZag(A, order)
