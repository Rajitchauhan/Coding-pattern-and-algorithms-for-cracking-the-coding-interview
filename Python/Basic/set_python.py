"""

A set is an unordered collection of items.
Every set element is unique (no duplicates) and must be immutable (cannot be changed).

However, a set itself is mutable. We can add or remove items from it.

Sets can also be used to perform mathematical set operations like union,
intersection, symmetric difference, etc.

"""
s = set() # set

s1 = {} # dict
set1 = {1 , 2}

print(type(set1))

set1.add(3)
print(set1)

set1.update([4,5])
print(f'set one ::  {set1}')

set2 = {1,2,5,6,7,8,9}
print(f'set two ::  {set2}')
####################################################################################
####################################################################################
####################################################################################
""" set operations """

#union
print(" union of two sets ",set1 | set2)

#inntersaction

print("intersaction of two sets ",set1 & set2)

# Set Difference

print(" Difference of two sets ",set1 - set2)


# Set Symmetric Difference

print("Set Symmetric Difference :: " , set1 ^ set2)
