class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr = []
        while head is not None:
            arr.append(head.val)
            head = head.next
        ret = 0
        for i in range(len(arr)):
            ret = max(ret, arr[i]+arr[len(arr)-i-1])
        return ret

'''
Key ideas of this problem include:
1. Either creating an array and summing based on index and index from end.
2. OR finding the middle of a linked list, reversing the second half and 
    suming across the rest of the list from the start of each half.
3. Return the max sum of those pairs.
'''