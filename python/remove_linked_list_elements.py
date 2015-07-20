# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):
        while(head):
            if head.val == val:
                head = head.next
            else:
                break
        if not head:
            return head
        current = head
        while(current.next):
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
                if not current:
                    break
        return head
