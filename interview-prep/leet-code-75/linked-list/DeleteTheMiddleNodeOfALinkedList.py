class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return None
        elif head.next.next is None:
            head.next = None
            return head
        cur = head
        fast = head.next.next
        slow = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        slow.next = slow.next.next
        return cur

'''
Key ideas of the problem include:
1. using fast and slow pointers to determine the middle of the linked list
2. Deleting that middle node and returning the modified linked list (i.e. head pointer)
'''