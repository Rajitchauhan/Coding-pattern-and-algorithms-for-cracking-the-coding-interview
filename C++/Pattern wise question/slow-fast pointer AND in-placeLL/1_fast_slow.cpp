#include <iostream>

bool hasCycle(Node* head){
 Node* fast , *slow;
 fast=head;
 slow=head;
 while(fast != nullptr && fast->next != nullptr){
    slow = slow->next;
    fast = fast->next->next;

    if(slow==fast){
        return true;
    }
    return false;
 }

}


