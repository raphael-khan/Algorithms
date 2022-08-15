# Write a function to delete a node in a singly-linked list. You will not be given access to the head of the list, instead you will be given access to the node to be deleted directly.

# It is guaranteed that the node to be deleted is not a tail node in the list.

head = [4,5,1,9] 
node = 5
Output = [4,1,9]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        node.val = node.next.val # make a copy of the next node [4,1,1,9]
        node.next = node.next.next # point the reference of the node to next next node to get the desired value. 
        