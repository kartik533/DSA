A = [10, 20, 30, 50, 50, 60, 70, 80, 90, 100]
K = 65


# First we have to find the bounds to apply binary search
def binarySearch(A, K):
    low, high = findBounds(A, K)
    while low <= high:
        mid = low + (high - low) // 2

        if K < A[mid]:
            high = mid - 1
        if K > A[mid]:
            low = mid + 1
        if K == A[mid]: a
        return mid
    return -1


def findBounds(A, key):
    low, high, val = 0, 1, A[0]

    while val < key:
        low = high
        high = 2 * high
        val = A[high]

    return (low, high)  # set containing low and high indices
