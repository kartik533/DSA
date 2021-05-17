A = [[1, 2, 3, 4],
     [2, 3, 4, 5],
     [8, 6, 5, 4],
     [0, 9, 8, 7]]


def rotateMatrix(A):
    res = []
    while A and A[0]:
        temp = []
        for row in A:
            # print(row)
            temp.append(row.pop())
        res.append(temp)
    return res


print(rotateMatrix(A))
