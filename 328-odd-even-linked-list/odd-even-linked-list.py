# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def f(self, cur: ListNode) -> Optional[ListNode]:
        # Base case
        if cur.next is None:
            return cur.next
        
        new_next = self.f(cur.next)

        # Reassign cur.next
        # Return original cur.next

        original_next = cur.next
        cur.next = new_next

        return original_next 

    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        second_head = self.f(head)
        #1 -> 3 -> 5   2 -> 4
        tail = head
        while tail.next is not None: #trong khi no chua phai nut tail, nut cho~ khac None
            tail = tail.next
        
        tail.next = second_head

        return head
        