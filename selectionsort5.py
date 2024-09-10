# selection sort 
# it select smallest element of array and compare it with first element of array then swap smaller element at first(0) index
def selectionsort(arr,high):
    for i in range(high - 1):
        min_idx = i
        for j in range(i + 1, high):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i] ,arr[min_idx] = arr[min_idx], arr[i]

def printarray(arr):
    for i in range(len(arr)-1):
        print(arr[i], end=" ")
    print()

if __name__ == "__main__":
    arr = [2,3,1,5,6,8,3,2]
    high = len(arr)
    selectionsort(arr,high)
    printarray(arr)
    
