from typing import Optional
class ListNode:
    def __init__(self, val = 0 , next = None):
        self.val = val
        self.next = next

class Solution:
    def _reverseLinkedlist(self, head: Optional[ListNode]) -> Optional[ListNode] :
        current = head
        prev = None

        while current:
            next_node = current.next
            current.next = prev

            current = next_node
            prev = current
        return prev

head = [1]
head = [2]
out = Solution()
out._reverseLinkedlist(head)