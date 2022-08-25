""" stack - it is linear ds which follow LIFO(last in first out) Ex - undo function
using collections """

def create_stack():
	stack = []
	return stack

def push(stack , item):
	stack.append(item)

def is_empty(stack):
	if len(stack) == 0:
		print('stack is  empty')
	else:
		print("not empty")


def Pop(stack):
	if(is_empty(stack)):
		print("stack is empty")
	else:
		stack.pop()
		

def view(stack):
	l = len(stack)
	for x in range(l):
		print(stack[x] , end=" ")

stack = create_stack()
is_empty(stack)

push(stack , 1)
push(stack , 2)
push(stack , 3)
push(stack , 4)
push(stack , 5)
view(stack)
is_empty(stack)
print("pop 5 " , Pop(stack))
print("pop 4 " , Pop(stack))

view(stack)


