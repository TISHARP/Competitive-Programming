def findIndexBinary(arr, val):
    left = 0
    right = len(arr)-1
    while left < right:
        mid = (l+r)>>1
        if arr[mid] == val:
            return mid
        elif arr[mid] < val:
            left = mid+1
        else:
            right = mid-1
    return -1

'''
Key ideas of this algorithm include:
1. Looking at the middle of a range of values and then depending on how that index
    relates to the value you are looking for setting the left or right side of
    the range to be the middle value + (for left) or - (for right) 1 of the middle
    Edventually your range will find the value or your range will collapse returning -1
2. If you don't find the value return -1
'''