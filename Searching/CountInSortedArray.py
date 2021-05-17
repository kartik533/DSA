A = [10, 20, 30, 50, 50, 50, 70, 80, 90, 100]
K = 50

def countInSortedArray(A,K):
    low = 0
    high = len(A)-1
    while low <= high:
        mid = low + (high-low)//2

        if K<A[mid]:
            high = mid - 1
        if K>A[mid]:
            low = mid + 1
        if K == A[mid]:
            return mid
    return -1

print(binarySearch(A,K))

