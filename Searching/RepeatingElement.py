A = [0,1,4,1,2]

def repeatingElement(A):
    for i in range(len(A)):
        if A[abs(A[i])]>= 0:
            A[abs(A[i])] = -1*A[abs(A[i])]
        else:
            return abs(A[i])

print(repeatingElement(A))
