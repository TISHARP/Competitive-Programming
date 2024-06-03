def findIndexLinear(arr,val):
    for i in range(arr):
        if arr[i]==val:
            return i
    return -1

'''
Key ideas of this algorithm include:
1. Looking at each element sequentially (linearly) until you find the value
2. If you don't find the value return -1
'''