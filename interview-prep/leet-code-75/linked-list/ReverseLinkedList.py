class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head
        while cur:
            nextt = cur.next
            cur.next = prev
            prev = cur
            cur = nextt
        return prev

'''
Key ideas of this problem include:
1. Swapping the order of the elements based on the next values.
2. Returning that modified modified list
'''