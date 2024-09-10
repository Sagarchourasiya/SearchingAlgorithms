# binary algorithm
# binary search divide array into half    if mid[halfarray] == key element found
# else if array of mid arr[mid] and key is greater than array of mid then find element in right side of array
# if key is less than arr[mid] find element on left side 
def binarysearch(arr,low,high,key):
    while low <= high:
        mid = low + (high - low) // 2
        # divide array into half to find mid (ex,7//2 = 3 ,so mid = 3index)
        if arr[mid] == key:  #if mid(arr[3] = 1 ) == key( value 6)
            return mid       # key = mid = arr[i] 
        if arr[mid] < key:   # ex 6 < arr[3] , then low(arr[0]) = mid (mid = 3) + 1(arr[4] == key)
            low = mid + 1 
        else:                # high(5) = mid (3) - 1 [arr[3-1] 6 == key]
            high = mid - 1
    return -1
if __name__ == "__main__":
    arr = [9,3,6,1,5,2,3]
    n = len(arr)
    key = 3
    answer = binarysearch(arr, 0, n -1, key)
    if (answer == -1):
        print("Element Not Found in Array")
    else:
        print("Element is Found At Index",answer)
    