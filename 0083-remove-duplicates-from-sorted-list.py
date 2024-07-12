# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        org = head.next
        while org:
            try:
                if org.val == org.next.val:
                    org.next = org.next.next
                    continue
            except:
                break
            org = org.next
    
        if head.val == head.next.val:
            head = head.next
        return head