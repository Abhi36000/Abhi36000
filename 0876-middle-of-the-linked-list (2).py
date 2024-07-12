# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        first_ptr = head
        second_ptr = head
        while first_ptr and first_ptr.next:
            second_ptr = second_ptr.next
            first_ptr = first_ptr.next.next
        return second_ptr