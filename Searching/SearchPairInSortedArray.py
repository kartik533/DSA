A = [2,7,11,15]


def searchForPair(A, target):
    left, right = 0, len(A) - 1

    while left <= right:
        if A[right] + A[left] == target:
            return (A[right], A[left])
        if A[right] + A[left] > target:
            right -= 1
        if A[right] + A[left] < target:
            left += 1
    return -1

print(searchForPair(A,9))
