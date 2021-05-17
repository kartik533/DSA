A = [10, 20, 20, 50, 50, 60, 70, 80, 90, 100]
K = 50


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
            if mid == 0 or A[mid - 1] != A[mid]:
                return mid  # this is the first occurence then
            else:
                high = mid - 1
    return -1


print(binarySearch(A, K))
