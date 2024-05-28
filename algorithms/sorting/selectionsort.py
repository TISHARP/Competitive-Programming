def selectionSort(arr):
    for i in range(len(arr)-1):
        midx = i #find the minimum element if the rest of the array
        for j in range(i+1,len(arr)):
            if arr[midx] > arr[j]:#if this element is smaller than the min, set the min to this index
                midx = j
        arr[i],arr[midx]=arr[midx],arr[i] #swap the current index with the minimum index.

'''
Key ideas of the selection sort include:
1. Looping through an entire array.
2. Finding the minimum index of the remaining array
3. Using our loop variable to make a swap with whatever value is the minimum
Pros:
Simple to understand and slightly more efficient than bubble sort.
Cons:
Very slow when array is large.
'''