def partition(arr,l,h):
    pivot = arr[h]
    i = l-1
    for j in range(l,h):
        if arr[j] <= pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[h]=arr[h],arr[i+1]
    return i+1
def quicksort(arr,l,h):
    if l < h:
        p = partition(arr,l,h)
        quicksort(arr,l,p-1)
        quicksort(arr,p+1,h)

'''
Key ideas of the quick sort include:
1. Quick sort is a divide and conquer sorting strategy
2. We choose a pivot in the middle of a range
    we will do this recursively
3. Then we compare elements that are left and right of that pivot
    we can swap these elements in cases we need to do so.
4. Once we sort the left and right sides of all sub partitions with their respective pivots we are done.
Pros:
Very good runtime in real world cases making it super fast.
Fast average execution time O(n*log n ) time complexity.
Great for large arrays
Cons:
Could lead to O(n^2) time complexity in worst case scenarios
Not good for small arrays
Elements with the same values (by sort) might switch relative order in array.
'''