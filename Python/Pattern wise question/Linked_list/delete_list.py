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

    def delete_list(self):
        curr = self.head
        while curr:
            pre = curr.next
            del curr.data
            curr = pre

	def printList(self):
		temp = self.head
		while(temp):
			print(temp.data)
			temp = temp.next

	def length(self):
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

	def insert_at_postion(self , data , pos):
		if pos < 0 or pos >= self.length():
			raise Exception("invalid position ")
		else:
			if pos == 0:
				self.insert_at_start(data)
			elif pos == self.length()-1:
				self.insert_at_end(data)
			else:
				temp = self.head
				for _ in range(pos-1):
					temp =temp.next
				newnode = Node(data)
				newnode.next = temp.next
				temp.next = newnode

    #n = Node(10)
#print(n.data)
ll = Linked_list()
ll.insert_at_start(5)
ll.insert_at_start(10)
ll.insert_at_start(2)
#ll.printList()
ll.length()
ll.insert_at_end(20)
ll.insert_at_end(30)
ll.insert_at_end(12)
ll.printList()
ll.delete_list()
print("after deletion ")
ll.printList()
