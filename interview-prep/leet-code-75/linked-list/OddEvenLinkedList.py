class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        o = head
        e = head.next
        eh = e
        while e is not None and e.next is not None:
            o.next = o.next.next
            e.next = e.next.next
            o = o.next
            e = e.next
        o.next = eh
        return head

'''
Key ideas of the problem include:
1. Collecting the even indexes and collecting the odd indexes
2. Combine the even value index after the odd value indexes
    and return the modified list.
'''