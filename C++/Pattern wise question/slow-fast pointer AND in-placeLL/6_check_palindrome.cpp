
#include <iostream>
using namespace std;

class Node{
  public:
  int data;
  Node* next;

  Node(int data){
    this->data = data;
    this->next = NULL;
  }

};

class Solution {
public:
    ListNode* reverse(ListNode* head){
        ListNode* curr =  head;
        ListNode* pre = NULL;
        ListNode* nxt = NULL;
        while(curr){
            nxt = curr->next;
            curr->next = pre;
            pre = curr;
            curr = nxt;
        }
        return pre;

    }

    ListNode* getMid(ListNode* head){
        ListNode* fast =  head;
        ListNode* slow = head;

        while(fast != NULL and fast->next != NULL){
            slow = slow->next;
            fast = fast->next->next;
        }
        return  slow;

    }
    bool isPalindrome(ListNode* head) {
       if(head == NULL or head->next == NULL) return true;
       ListNode* mid = getMid(head);
       ListNode* head2  = reverse(mid);
       ListNode* head1 = head;
       while(head1 != NULL and head2 != NULL){
           if(head1->val != head2->val){
               return false;
           }
           head1 = head1->next;
           head2 = head2->next;
       }
        return true;
    }
};

/*

ListNode* getmid(ListNode*head){
      ListNode* slow = head;
      ListNode* fast = head->next;
      while(fast !=NULL && fast->next !=  NULL){
          slow=slow->next;
          fast = fast->next->next;
      }
      return slow;
  }

  ListNode * reverse(ListNode* head){
      ListNode* temp = NULL;
      ListNode* cur = head;
      ListNode * prev = NULL;

      while(cur != NULL){
          temp=cur->next;
          cur->next = prev;
          prev = cur;
          cur = temp;
      }
      return prev;
  }

    bool isPalindrome(ListNode* head) {
        if(head->next == NULL){
            return true;
        }
        //step-1 get mid.
        ListNode* mid = getmid(head);
        //step-2 reverse after mid
        ListNode* temp = mid->next;
        mid->next = reverse(temp);
        //step-3 compare both half.

        ListNode*head1 = head;
        ListNode*head2 = mid->next;

        while(head2 != NULL){
            if(head2->val != head1->val) return false;

            head1=head1->next;
            head2 = head2->next;
        }

        //step-4 repeat reverse so we can get orignal list.

        // temp = mid->next;
        // mid->next = reverse(temp);
        return true;
    }



    class Solution {
public:
    bool isPalindrome(ListNode* head) {
        ListNode *slow = head, *fast = head, *prev, *temp;
        while (fast && fast->next)
            slow = slow->next, fast = fast->next->next;
        prev = slow, slow = slow->next, prev->next = NULL;
        while (slow)
            temp = slow->next, slow->next = prev, prev = slow, slow = temp;
        fast = head, slow = prev;
        while (slow)
            if (fast->val != slow->val) return false;
            else fast = fast->next, slow = slow->next;
        return true;
    }
};
*/
