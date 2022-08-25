"""
Global Variables
In Python, a variable declared outside of the function or in global scope is known as a global variable. This means that a global variable can be accessed inside or outside of the function.

Let's see an example of how a global variable is created in Python.

Example 1: Create a Global Variable

x = "global"

def foo():
    print("x inside:", x)


foo()
print("x outside:", x)
Output

x inside: global
x outside: global

"""
x = "global"
y = 20

def foo():
    print("x inside:", x)
    print("y inside:", y)


foo()
print("x outside:", x)
print("y outside:", y)

""" What if you want to change the value of x inside a function? """

x = "global"

def foo():
    x = x * 2
    print(x)

foo()

""" UnboundLocalError: local variable 'x' referenced before assignment
    The output shows an
     error because Python treats x as a local variable and x is also not defined inside foo().

  """

"""
Accessing local variable outside the scope
def foo():
    y = "local"


foo()
print(y)
Output

NameError: name 'y' is not defined
The output shows an error because we are trying to access a local variable y in a global scope whereas the local variable only works inside foo() or local scope.

Let's see an example on how a local variable is created in Python.

Example 3: Create a Local Variable
Normally, we declare a variable inside the function to create a local variable.

def foo():
    y = "local"
    print(y)

foo()
Output

local

"""
