# Insertion sort algorithm
# in insertion sort we start checking element from 1 index and traverse from left to rigth to sort all elements of array
def insertionsort(arr,n):
    for i in range(1,n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def printarray(arr):
    for i in range(n):
        print(arr[i], end=" ")
    print
if __name__ == "__main__":
    arr = [2,7,8,4,5,3]
    n = len(arr)
    insertionsort(arr,n)
    printarray(arr)
    
