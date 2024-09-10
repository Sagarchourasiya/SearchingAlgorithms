# bubble sort
# bubble sort compare adjcent element in array 
# if first element is geater swap to next element
def bubblesort(arr,n):
    for i in range(n):
        swapped = False
        for j in range(0,n-i-1):
            if arr[j] > arr[j + 1]:
                arr[j] , arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if (swapped == False):
          break
if __name__ == "__main__":
    arr = [90,34,26,11,9,56]
    n = len(arr)
    bubblesort(arr,n)
    for i in arr:
        print(i, end=" ")