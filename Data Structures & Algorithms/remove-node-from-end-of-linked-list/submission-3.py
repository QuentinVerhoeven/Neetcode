# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        #get a pointer n nodes away from head, then run lilke a sliding window
        dummy = ListNode(0, head)
        trail,lead = dummy,head

        count = 0
        while count < n:
            lead = lead.next
            count += 1
        
        while lead is not None:
            trail = trail.next
            lead = lead.next

        #delete node
        trail.next = trail.next.next
        return dummy.next










