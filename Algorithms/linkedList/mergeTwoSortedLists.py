# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.


l1 = [1,2,4] 
l2 = [1,3,4]
Output = [1,1,2,3,4,4]

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1:ListNode, l2:ListNode) -> ListNode:
        dummy = ListNode() # create a dummy node and add all nodes to it to handle edge case. 
        curr = dummy 

        while l1 and l2:   # when both are non empty / non null
            if l1.val < l2.val: # if l1 value is less than l2, then add that l1 node to curr.
                curr.next = l1
                l1 = l1.next     # update l1 pointer.
            else:                # if l2 is less or equal then add l2 node to curr
                curr.next = l2
                l2 = l2.next     # update l2 pointer. 

            curr = curr.next     # update curr pointer regardless of whatever node is added. 

        if l1:                   # edge case if one list is empty. if l1 is not null, if l2 is not null. 
            curr.next = l1
        elif l2:
            curr.next = l2

        return dummy.next

        