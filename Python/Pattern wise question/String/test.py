from collections import deque

def create_Quequ():
	queqe = deque()

def enqueqe(queqe , item):
	queqe.appendleft(item)
def is_empty():
	return len(queqe)==0
def Deque(queqe):
	if(is_empty()):
		print("queqe is empty")
	else:
		queqe.pop()
def view(queqe):
	if len(queqe)<=1:
		for i in range(len(queqe)):
			print(queqe[i] , end=" ")
queqe = create_Quequ()
enqueqe(queqe , 1)
enqueqe(queqe , 2)
enqueqe(queqe , 3)
enqueqe(queqe , 4)
view(queqe)
print("pop 1 "+Deque(queqe))
print("pop 2 "+Deque(queqe))
view(queqe)
