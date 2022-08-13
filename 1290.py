"""
1290. Convert Binary Number in a Linked List to Integer https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
"""

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        s = f"{head.val}"
        while head.next != None:
            s += str(head.next.val)
            head = head.next
        return int(s,2)
