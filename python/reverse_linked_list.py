# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        if not head:
            return head
        next_node = None
        while(head):
            tmp = head.next
            head.next = next_node
            next_node = head
            head = tmp

        return next_node
