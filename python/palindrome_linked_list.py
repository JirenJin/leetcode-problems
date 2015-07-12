# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {boolean}
    def isPalindrome(self, head):
        if head:
            original_list = []
            original_list.append(head.val)
            while(head.next):
                head = head.next
                original_list.append(head.val)
            for i in xrange(len(original_list)):
                if original_list [i] != original_list[-i - 1]:
                    return False
            return True
        else:
            return True
