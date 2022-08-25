class Solution {
public:
    ListNode* oddEvenList(ListNode* head) {
        if(head == NULL or head->next == NULL)
            return head;

        ListNode* even , *odd , *EVEN;
        odd = head;
        even = head->next;
        EVEN = even;
        while(odd->next and even->next){
            odd->next = odd->next->next;
            even->next = even->next->next;

            odd = odd->next;
            even =even->next;
        }
        odd->next = EVEN;
        return head;
    }
};
