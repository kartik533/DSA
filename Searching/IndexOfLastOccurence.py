A = [10, 20, 20, 50, 50, 60, 70, 90, 90, 100]
K = 90

def binarySearch(A, K):
    low = 0
    high = len(A) - 1
    while low <= high:
        mid = low + (high - low) // 2

        if K < A[mid]:
            high = mid - 1
        elif K > A[mid]:
            low = mid + 1
        else:
            if mid == len(A)-1 or A[mid + 1] != A[mid]:
                return mid  # this is the last occurence then
            else:
                low = mid + 1
    return -1


print(binarySearch(A, K))
