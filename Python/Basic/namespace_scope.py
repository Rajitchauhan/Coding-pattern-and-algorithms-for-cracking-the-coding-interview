"""
namespace - it is collection of names

#########################################

A scope is the portion of a program from where a namespace can be accessed directly without any prefix.

At any given moment, there are at least three nested scopes.

Scope of the current function which has local names
Scope of the module which has global names
Outermost scope which has built-in names
When a reference is made inside a function, the name is searched in the local namespace, then in the global namespace and finally in the built-in namespace.

If there is a function inside another function, a new scope is nested inside the local scope.

"""

def outer_function():
    a = 20

    def inner_function():
        a = 30
        print('a =', a)

    inner_function()
    print('a =', a)

a = 10
outer_function()
print('a =', a)

"""
As you can see, the output of this program is

a = 30
a = 20
a = 10

"""
print()
def outer_function():
    global a
    a = 20

    def inner_function():
        global a
        a = 30
        print('a =', a)

    inner_function()
    print('a =', a)


a = 10
outer_function()
print('a =', a)

"""
The output of the program is.

a = 30
a = 30
a = 30

"""
