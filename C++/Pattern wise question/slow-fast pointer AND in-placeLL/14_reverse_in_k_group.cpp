/**
25. Reverse Nodes in k-Group
Hard

8615

527

Add to List

Share
Given the head of a linked list,
 reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list.
If the number of nodes is not a multiple of k then left-out nodes,
in the end, should remain as it is.

You may not alter the values in the list's nodes,
only nodes themselves may be changed.



Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
Example 2:


Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]

*/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    int getLen(ListNode* head){
        ListNode* curr = head;
        int count=0;
        while(curr){
            count += 1;
            curr = curr->next;
        }
        return count;
    }
    ListNode* reverseKGroup(ListNode* head, int k) {
        if(k <= 1 or head == NULL)
            return head;

        ListNode* curr = head , *pre = NULL;
        int len = getLen(head);

        if(len < k)
            return head;
         int no_of_group_to_be_reverse = len / k;

        for(int i=0; i <no_of_group_to_be_reverse; i++){
            ListNode* last_node_of_first_list = pre;
            ListNode* last_node_of_sub_list = curr;

            ListNode *temp = nullptr;

            for(int i=0; i < k; i++){
                temp = curr->next;
                curr->next = pre;
                pre = curr;
                curr = temp;
            }
            if(last_node_of_first_list != NULL){
                last_node_of_first_list->next = pre;
            }
            else{
                head = pre;
            }

            last_node_of_sub_list->next = curr;

            if(curr == NULL){
                break;
            }
            pre = last_node_of_sub_list;
        }
         return head;

    }
};


// recursive

Solution 1:(Recursion)

Approach:

1) The first step is to check whether the Head is NULL or Not,
 if its NULL then we can directly return NULL,
2) If the Head is not NULL,
 then we need to check the length of Linked List starting from current Head.
3) If it is not a multiple of K(Less than K) ,
 then there is no need to reverse it and hence we can directly return head,
4) Else if its a multiple of K,
 then we have to reverse the K elements starting from current Head,
5) We will follow the same steps for the rest of the elements Recursively.

class Solution {
public:
    ListNode* reverseKGroup(ListNode* head, int k)
    {
        if(!head)
            return NULL;
        ListNode *KSizeChecker = head;
        for(int i=0;i<k;i++)
        {
            if(KSizeChecker==NULL)
                return head;
            KSizeChecker = KSizeChecker->next;
        }
        int cnt=0;
        ListNode *cur=head,*prev=NULL,*next=NULL;
        while(cur and cnt<k)
        {
            next=cur->next;
            cur->next=prev;
            prev=cur;
            cur=next;
            cnt++;
        }
        if(next)
            head->next=reverseKGroup(next,k);
        return prev;
    }
};
