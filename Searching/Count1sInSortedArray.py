A = [0]
n = len(A)


def count1s(A, n):
    low = 0
    high = n - 1
    firstOccurence = 0

    while low <= high:
        mid = low + (high - low) // 2

        if 1 < A[mid]:
            high = mid - 1
        elif 1 > A[mid]:
            low = mid + 1
        else:
            if mid == 0 or A[mid - 1] != A[mid]:
                return n-mid
            else:
                high = mid - 1
    return 0


print(count1s(A, n))
