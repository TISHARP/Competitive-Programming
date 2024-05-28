def merge(array, left, mid, right):
    subArrayOne = mid - left + 1
    subArrayTwo = right - mid

    # Create temp arrays
    leftArray = [0] * subArrayOne
    rightArray = [0] * subArrayTwo

    # Copy data to temp arrays leftArray[] and rightArray[]
    for i in range(subArrayOne):
        leftArray[i] = array[left + i]
    for j in range(subArrayTwo):
        rightArray[j] = array[mid + 1 + j]

    indexOfSubArrayOne = 0  # Initial index of first sub-array
    indexOfSubArrayTwo = 0  # Initial index of second sub-array
    indexOfMergedArray = left  # Initial index of merged array

    # Merge the temp arrays back into array[left..right]
    while indexOfSubArrayOne < subArrayOne and indexOfSubArrayTwo < subArrayTwo:
        if leftArray[indexOfSubArrayOne] <= rightArray[indexOfSubArrayTwo]:
            array[indexOfMergedArray] = leftArray[indexOfSubArrayOne]
            indexOfSubArrayOne += 1
        else:
            array[indexOfMergedArray] = rightArray[indexOfSubArrayTwo]
            indexOfSubArrayTwo += 1
        indexOfMergedArray += 1

    # Copy the remaining elements of left[], if any
    while indexOfSubArrayOne < subArrayOne:
        array[indexOfMergedArray] = leftArray[indexOfSubArrayOne]
        indexOfSubArrayOne += 1
        indexOfMergedArray += 1

    # Copy the remaining elements of right[], if any
    while indexOfSubArrayTwo < subArrayTwo:
        array[indexOfMergedArray] = rightArray[indexOfSubArrayTwo]
        indexOfSubArrayTwo += 1
        indexOfMergedArray += 1

def mergeSort(array, begin, end):
    if begin >= end:
        return

    mid = begin + (end - begin) // 2
    mergeSort(array, begin, mid)
    mergeSort(array, mid + 1, end)
    merge(array, begin, mid, end)

#Above code provided by GeeksForGeeks https://www.geeksforgeeks.org/merge-sort/
'''
Key ideas of the merge sort include:
1. Merge sort is a divide and conquer sorting strategy
2. We divide the arrays into halves recursively then sort those partitions individually.
3. Then we merge the arrays back together.
Pros:
Consistent runtime in best and worst case scenarios
Decently fast execution with O(n*log n ) time complexity
Cons:
Very large implementation.
Also not good in cases of already sorted arrays.
'''