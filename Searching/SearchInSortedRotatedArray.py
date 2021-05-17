A = [3,1]


def searchINSortedRotatedArray(A, target):
    low, high = 0, len(A) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if A[mid] == target:
            return mid

        if A[low] <= A[mid]:
            if target >= A[low] and target < A[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if target > A[mid] and target <= A[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1


print(search(A, 1))
