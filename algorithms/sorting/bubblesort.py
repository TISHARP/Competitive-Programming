def bubbleSort(arr): #simple bublesort implementation for simple comparisons.
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]: #If the current element is greater than the next element swap them.
                arr[j],arr[j+1]=arr[j+1],arr[j] #just a swap

'''
Key ideas of the bubble sort include:
1. comparing adjacent elements
2. if elements are in wrong order swap them
3. do this until you are sure no other swaps can occur.
Pros:
Simple to understand.
Cons:
Very slow when array is large.
'''