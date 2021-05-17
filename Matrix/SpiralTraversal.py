A = [[1, 2, 3, 4],
     [2, 3, 4, 5],
     [8, 6, 5, 4],
     [0, 9, 8, 7]]


def spiralMatrix(A):
    res = []
    while A:
        res += A.pop(0)
        if A and A[0]:
            for row in A:
                res.append(row.pop())
        if A and A[0]:
            res += A.pop()[::-1]
        if A and A[0]:
            for row in A[::-1]:
                res.append(row.pop(0))
    return res


print(spiralMatrix(A))
