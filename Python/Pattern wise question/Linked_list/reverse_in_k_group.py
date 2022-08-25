"""
25. Reverse Nodes in k-Group
Hard

8615

527

Add to List

Share
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.



Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
Example 2:


Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]


Constraints:

The number of nodes in the list is n.
1 <= k <= n <= 5000
0 <= Node.val <= 1000


Follow-up: Can you solve the problem in O(1) extra memory space?

"""
print("jai ho radhey krishna ")


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getLen(self , head):
        count=0
        curr  = head
        while(curr):
            count += 1
            curr = curr.next
        return count
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if(k <= 1 or head == None):
            return head

        curr = head
        pre = None

        listLen = self.getLen(head)
        if(listLen < k):
            return head;

        list_to_be_reverse = listLen // k

        for i in range(list_to_be_reverse):
            last_node_of_first_list = pre
            last_node_of_sub_list = curr
            nxt = None

            for j in range(k):
                nxt = curr.next
                curr.next = pre
                pre = curr
                curr = nxt

            if(last_node_of_first_list != None):
                last_node_of_first_list.next= pre
            else:
                head = pre

            
            last_node_of_sub_list.next = curr

            if(curr == None):
                break;
            pre = last_node_of_sub_list

        return head
