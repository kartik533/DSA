A = [[1, 2, 3, 4],
     [6, 7, 8, 9],
     [9, 10, 11, 12],
     [13, 14, 15, 16]]


# begin from top right corner
# if curr_element == k, return
# if k < curr_element , move towards in the same row
# if k > curr_elemnet, move to next column

#complexity = O(r+c)

def searchInSortedMatrix(A, k):
    for i in range(len(A)):
        for j in range(len(A)-1, -1, -1):
            if A[i][j] == k:
                return (i, j)
            if A[i][j] < k:
                break
            else:
                continue

    return -1

print(searchInSortedMatrix(A,20))
