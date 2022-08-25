struct Node
{
    int data;
    Node* next;

    Node(int x){
        this->data = x;
        this->next = NULL;
    }
};


class Solution
{
    public:
    Node* reverse(Node* head){
        Node* curr = head;
        Node* pre = NULL;
        Node* nxt = NULL;
        while(curr){
            nxt = curr->next;
            curr->next = pre;
            pre = curr;
            curr = nxt;
        }
        return pre;

    }
    Node* addOne(Node *head)
    {
        // Your Code here
        // return head of list after adding one
        head = reverse(head);
        Node* curr = head;
        while(curr){
            if(curr->next == NULL and curr->data == 9){
                curr->data = 1;
                Node* newnode = new Node(0);
                newnode->next = head;
                head = newnode;
                curr = curr->next;
            }
            else if(curr->data == 9){
                curr->data = 0;
                curr = curr->next;
            }
            else{
                curr->data = curr->data+1;
                curr = curr->next;
                break;
            }
        }
        head = reverse(head);
        return head;
    }
};

//{ Driver Code Starts.

int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        string s;
        cin>>s;

        Node* head = new Node( s[0]-'0' );
        Node* tail = head;
        for(int i=1; i<s.size(); i++)
        {
            tail->next = new Node( s[i]-'0' );
            tail = tail->next;
        }
        Solution ob;
        head = ob.addOne(head);
        printList(head);
    }
    return 0;
}
