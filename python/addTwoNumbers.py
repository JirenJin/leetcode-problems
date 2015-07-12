# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        a0 = ListNode(0)
        answer = a0
        carry = 0
        while l1 and l2:
            sum = l1.val + l2.val + carry
            a1 = ListNode(sum % 10)
            a0.next = a1
            a0 = a1
            carry = sum / 10
            l1 = l1.next
            l2 = l2.next

        while l1:
            sum = l1.val + carry
            a1 = ListNode(sum % 10)
            a0.next = a1
            a0 = a1
            carry = sum / 10
            l1 = l1.next

        while l2:
            sum = l2.val + carry
            a1 = ListNode(sum % 10)
            a0.next = a1
            a0 = a1
            carry = sum / 10
            l2 = l2.next

        if carry > 0:
            a1 = ListNode(carry)
            a0.next = a1

        return answer.next
