def countingsort(input_array):
    M = max(input_array)

    count_sort = [0]* (M + 1)

    for num in input_array:
        count_sort[num] += 1
    
    for i in range(1,M+1):
        count_sort[i] += count_sort[i - 1]
    output_array = [0] * len(input_array)

    for i in range(len(input_array)):
        output_array[count_sort[input_array[i]] - 1] =input_array[i]
        count_sort[input_array[i]] -= 1
    return output_array

if __name__ == "__main__":
    input_array = [9,34,21,76,43]
    output_array = countingsort(input_array)
    for num in output_array:
        print(num, end=" ")
