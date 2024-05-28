def insertionSort(arr):
    for i in range(1,len(arr)):
        key = arr[i]#select element to look at.
        j = i-1#start looking at elements that are before our focused element
        while j >= 0:
            if key < arr[j]: break #if our key is less than this element, we have found a place to swap.
            arr[j+1] = arr[j]
        arr[j+1] = key #swap the elements found.

'''
Key ideas of the insertion sort include:
1. Looping through the array starting on the second index 
    (if the length is 1 or less the array is already sorted)
2. That loop index will become our key or focused index.
3. we can compare elements with indices less than our key index.
    If that key element is less than any of those values, we need to make a swap
    We can then swap the index.
4. However if the key index is not less than any of those values, we need to continue looking
    If no index is every matched then that means our key index is our smallest index.
    We can then make the swap with that index (which will be 0 ultimately)
    otherwise see point 3.
'''