from typing import Optional
class listNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution :
    def mergeTwosorted(self, list1: Optional[listNode], list2: Optional[listNode]) -> Optional[listNode] :
        dummy = listNode()
        current = dummy

        while list1 and list2:
            if list1 < list2:
                current.next = list1
                list1 = list1.next

            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        current.next = list1 if list1 else list2
    
        return dummy
    