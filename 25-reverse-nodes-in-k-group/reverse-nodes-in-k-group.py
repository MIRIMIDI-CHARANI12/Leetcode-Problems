# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        previous = dummy

        while True:
            last = previous

            for i in range(k):
                last = last.next
                if last is None:
                    return dummy.next

            next_group = last.next
            prev = next_group
            current = previous.next
            while current != next_group:
                temp = current.next
                current.next = prev
                prev = current
                current = temp
            temp = previous.next
            previous.next = last
            previous = temp