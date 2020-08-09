class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode()
        pointer = res

        while l1 != None and l2 != None:
            if l1.val < l2.val:
                pointer.next = l1
                pointer = l1
                l1 = l1.next
            else:
                pointer.next = l2
                pointer = l2
                l2 = l2.next
        
        if l1 != None:
            pointer.next = l1

        if l2 != None:
            pointer.next = l2

        return res.next