def partition(arr,low,high):
    pivot = arr[high]
    i = low - 1
    for j in range(low,high):
        if arr[j] <= pivot:
            i += 1
            arr[j],arr[i]=arr[i],arr[j]
    arr[i + 1],arr[high]=arr[high],arr[i + 1]
    return i + 1

def quicksort(arr,low,high):
    if low < high:
        pi = partition(arr,low,high)
        quicksort(arr,low,pi - 1)
        quicksort(arr,pi +1,high)

def printarray(arr):
    for i in range(high):
        print(arr[i], end= " ")
    print()
    
if __name__ == "__main__":
    arr = [23,24,3,4,56,54]
    high = len(arr)
    print("Array before quick sort")
    printarray(arr)
    quicksort(arr,0,high-1)

    print("Array After quick sort")
    printarray(arr)