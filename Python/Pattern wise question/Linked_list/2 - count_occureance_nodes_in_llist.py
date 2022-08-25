#Count no of times a given occurance in linked list.
class Node:
    def __init__(self , data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def push(self, new_data):

        # Create a new Node
        new_node = Node(new_data)

        # 3. Make next of new Node as head
        new_node.next = self.head

        # 4. Move the head to point to new Node
        self.head = new_node

    def count_occurance(self , search_for):
        curr = self.head
        count = 0
        while curr != None:
            if curr.data== search_for:
                count += 1
            curr = curr.next

        return count

llist = Linkedlist()
llist.push(1)
llist.push(3)
llist.push(1)
llist.push(2)
llist.push(1)

# Check for the count function
print ("count of 1 is" , llist.count_occurance(1))
