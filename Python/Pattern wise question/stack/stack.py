#Using list .

from collections import deque


def create_stack():
	stack = deque()
	return stack

def push(stack , item):
	stack.append(item)

def is_empty(stack):
	return len(stack)== 0


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

stack = []
def isEmpty(self):
    return len(self.stack) == 0

def push(self, num):
    self.stack.append(num)

def pop(self):
    if self.isEmpty():
      raise Exception('Stack Underflow')
    return self.stack.pop()

def peek(self):
    if self.isEmpty():
        return None
    return self.stack[-1]
