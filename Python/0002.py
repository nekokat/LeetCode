"""
2. Add Two Numbers  https://leetcode.com/problems/add-two-numbers/
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s = l1.val+l2.val
        k = ListNode(s%10)
        p = s//10
        l = k
        while l1.next or l2.next:
            if l1.next is None:
                l1.next = ListNode()
            if l2.next is None:
                l2.next = ListNode()
            l1 = l1.next
            l2 = l2.next         
            s = l1.val+l2.val+p
            l.next = ListNode(s%10)
            l = l.next
            p = s//10
        if p:
            l.next = ListNode(1)
        return k
