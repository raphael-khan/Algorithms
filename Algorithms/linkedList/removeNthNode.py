# Given the head of a linked list, remove the nth node from the end of the list and return its head.

from .mergeTwoSortedLists import ListNode


Input = head = [1,2,3,4,5]
n = 2
Output = [1,2,3,5]
# key point is to figure out the end. One of the pointer has to point to the end. meaning point to null

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)  # initializing a dummy node 
        l, r = dummy # starting L, r pointers at dummy.
        # move r ahead n steps. 
        for i in range(n):
            r = r.next

        while r.next:
            r = r.next
            l = l.next

        l.next = l.next.next

        return dummy.next
        

        #hello world.




