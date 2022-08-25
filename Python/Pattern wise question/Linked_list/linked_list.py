class Node:
	def __init__(self ,  data):
		self.data = data
		self.next = None

class Linked_list:
	def __init__(self):
		self.head = None

	def insert_at_start(self , data):
		newnode = Node(data)
		newnode.next = self.head
		self.head = newnode

	def printList(self):
		temp = self.head
		while(temp):
			print(temp.data)
			temp = temp.next

	def  getLength(self):
		count = 0
		temp = self.head
		while(temp):
			temp = temp.next
			count += 1
		return count
		print('length is ::', +count)

	def insert_at_end(self , data):
		newnode = Node(data)
		if self.head:
			temp = self.head
			while temp.next:
				temp = temp.next
			temp.next = newnode
		else:
			self.head = newnode

	def delete_at_start(self):
		if self.head:
			pass
		else:
			print("Linked_list is empty ")



#n = Node(10)
#print(n.data)
ll = Linked_list()
ll.insert_at_start(5)
ll.insert_at_start(10)
ll.insert_at_start(2)
#ll.printList()
ll.getLength()
ll.insert_at_end(20)
ll.insert_at_end(30)
ll.insert_at_end(12)
ll.printList()
