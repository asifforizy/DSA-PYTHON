# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        dummy = ListNode(0, head)
        group_prev = dummy
        
        while True:
            # Check if there are at least k nodes left
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next
            
            group_next = kth.next
            
            # Reverse the group of k nodes
            prev, curr = kth.next, group_prev.next
            for _ in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            # Connect the previous group to the reversed group
            temp = group_prev.next
            group_prev.next = kth
            group_prev = temp
        
        return dummy.next