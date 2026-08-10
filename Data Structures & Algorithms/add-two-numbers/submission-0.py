# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        



        p1 = l1
        p2 = l2
        s1 = ""
        s2 = ""
        while p1 is not None:
            s1 = str(p1.val) + s1
            p1 = p1.next
        while p2 is not None:
            s2 = str(p2.val) + s2
            p2 = p2.next

        num = str(int(s1) + int(s2))

        #new linked list with number

        dummy = ListNode(0)
        p = dummy
        i = len(num) - 1
        while i >=0:
            p.next = ListNode(int(num[i]))
            i -= 1
            p = p.next
        return dummy.next