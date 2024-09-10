# linear search algorithm 
def linearsearch(arr, n, key):
    for i in range(0, n):
        if arr[i] == key:
            return i
    return -1
if __name__ == "__main__":
    arr = [3,4,2,9,5,1]
    n = len(arr)
    key = 1
    answer = linearsearch(arr, n, key)
    if (answer == -1):
        print("Element Not Found")
    else:
        print("Element Found at index ",answer)