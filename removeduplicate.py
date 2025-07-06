from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_duplicates(self, head: Optional[ListNode]):
    current = head
    while current and current.next:
        ans = current.next
        if current.val == ans.val:
            current.next = ans.next  # Skip duplicate
        else:
            current = current.next
    return head