from collections import deque

def create_Quequ():
	queqe = deque()
	return queqe

def Enqueqe(queqe , item):
	queqe.appendleft(item)
def is_empty():
	return len(queqe)==0
def Deque(queqe):
	if(is_empty()):
		print("queqe is empty")
	else:
		queqe.pop()
def view(queqe):
	if len(queqe)>=1:
		for i in range(len(queqe)):
			print(queqe[i] , end=" ")

queqe = create_Quequ()
Enqueqe(queqe , 1)
Enqueqe(queqe , 2)
Enqueqe(queqe , 3)
Enqueqe(queqe , 4)
view(queqe)
print("pop 1 ",Deque(queqe))
print("pop 2 ",Deque(queqe))
view(queqe)
