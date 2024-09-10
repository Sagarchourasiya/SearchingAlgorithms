# merge sort algorithm
# merge sort usage divide and conquer approach to solve a problem
# first it divide the hole array into two subarray 
# then it recursively compare these two subarray until element are in sorted order
def merge(arr,p,r,mid):
    L1 = mid - p + 1
    R1 = r - mid

    L = [0] * L1
    R = [0] * R1

    for i in range(L1):
        L[i] = arr[ p + i]

    for j in range(R1):
        R[j] = arr[mid + 1 + j]

    i = 0
    j = 0
    k = p

    while i < L1  and j < R1 :
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1 
        k += 1

    while i < L1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < R1:
        arr[k] = R[j]
        j += 1
        k += 1

def mergesort(arr, p, r):
    if p < r:
        mid = (p + r) // 2
        mergesort(arr, p, mid)

        mergesort(arr, mid + 1, r)

        merge(arr, p, r, mid)


def printarray(arr):
    for i in arr:
        print(i, end=" ")
    print()

if __name__ == "__main__":
    arr = [9,2,23,15,3,8,6]
    r = len(arr)
    print(f"Array before merge sort")
    printarray(arr)

    mergesort(arr, 0, r - 1)
    print("Array After merge sort")
    printarray(arr)