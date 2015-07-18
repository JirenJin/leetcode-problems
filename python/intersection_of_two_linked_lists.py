# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None
        else:
            lengthA = 1
            lengthB = 1
            nodeA = headA
            nodeB = headB
            while(nodeA.next):
                lengthA += 1
                nodeA = nodeA.next
            while(nodeB.next):
                lengthB += 1
                nodeB = nodeB.next
            if nodeA != nodeB:
                return None
            else:
                if lengthB > lengthA:
                    nodeB = headB
                    nodeA = headA
                    for i in xrange(lengthB - lengthA):
                        nodeB = nodeB.next
                elif lengthB < lengthA:
                    nodeB = headB
                    nodeA = headA
                    for i in xrange(lengthA - lengthB):
                        nodeA = nodeA.next
                else:
                    nodeB = headB
                    nodeA = headA
                while(nodeA):
                    if nodeA == nodeB:
                        return nodeA
                    nodeA = nodeA.next
                    nodeB = nodeB.next
