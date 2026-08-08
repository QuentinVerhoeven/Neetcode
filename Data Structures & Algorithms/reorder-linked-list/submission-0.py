# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #this one is thinking outside the box. Find the middle, 
        #reverse the 2nd half, and zipper merge
        
        #find midpoint
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        #cut everything before slow.next
        second = slow.next
        slow.next = None

        first = head


        #reverse second
        prev = None
        current = second
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        second = prev

        #merge now
        while first is not None and second is not None:
            first_next = first.next
            second_next = second.next
            
            first.next = second
            second.next = first_next

            first = first_next
            second = second_next


