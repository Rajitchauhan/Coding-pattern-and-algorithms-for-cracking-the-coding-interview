class Node:
    def __init__(self , data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):

        # Create a new Node
        new_node = Node(new_data)

        # 3. Make next of new Node as head
        new_node.next = self.head

        # 4. Move the head to point to new Node
        self.head = new_node

    def search(self , item):
        temp = self.head
        while temp:
            if temp.data == item:
                print("item found :: ",temp.data)
                return True
            temp = temp.next
        return False

if __name__ == '__main__':

    # Start with the empty list
    llist = LinkedList()

    ''' Use push() to construct below list
        14->21->11->30->10 '''
    llist.push(10);
    llist.push(30);
    llist.push(11);
    llist.push(21);
    llist.push(14);

    if llist.search(21):
        print("Yes")
    else:
        print("No")
