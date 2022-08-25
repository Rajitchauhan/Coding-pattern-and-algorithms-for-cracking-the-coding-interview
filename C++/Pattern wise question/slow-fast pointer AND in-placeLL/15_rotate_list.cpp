class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        if(k <=0 or head == NULL or head->next == NULL){
            return head;
        }
        ListNode* curr = head;
        ListNode* pre = NULL;
        int listLen = 0;
        while(curr){
            listLen += 1;
            pre = curr;
            curr = curr->next;
        }

        pre->next = head;
        k = k % listLen;

        int skip_list = listLen - k;

        for(int i=0; i < skip_list; i++){
            pre = head;
            head = head->next;
        }
        pre->next = NULL;

        return head;
    }
};
