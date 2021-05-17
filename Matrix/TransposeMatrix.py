A = [[1, 2, 3, 4],
     [2, 3, 4, 5],
     [8, 6, 5, 4],
     [0, 9, 8, 7]]


def transposeMatrix(A):
    res = []
    for i in range(len(A)):
        temp = []
        for j in range(len(A)):
            temp.append(A[j][i])
        res.append(temp)
    return res
print(transposeMatrix(A))
