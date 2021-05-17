A = [10, 20, 30, 50, 50, 60, 70, 80, 90, 100]
K = 100
low,high = 0,len(A)-1

def binarySearch(A,low,high,K):
    if low > high:
        return -1
    mid = low + (high-low)//2
    if A[mid] == K:
        return mid
    elif K < A[mid]:
        binarySearch(A,low,mid-1,K)
    else:
        binarySearch(A,mid+1,high,K)

print(binarySearch(A,low,high,K))



