# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} n
    # @return {ListNode}
    def removeNthFromEnd(self, head, n):
        # current is the node right before the one to be removed
        current = head
        current_plus_n = current
        while(n > 0):
            current_plus_n = current_plus_n.next
            n -= 1
        # if head is the node to remove
        if not current_plus_n:
            return head.next
        while(current_plus_n.next != None):
            current_plus_n = current_plus_n.next
            current = current.next
        current.next = current.next.next
        return head
