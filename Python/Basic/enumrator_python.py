"""
The enumerate() function returns an enumerate object.
It contains the index and value of all the items in the string as pairs.
This can be useful for iteration.

"""
GODs = ['Om namh shivay' , "OM" , "gauri mata" , "krishan G" , 'MAta rani']

st = "Shivay"

print(list(enumerate(st)))


for u in enumerate(GODs):
    print(u)

for numbers , ui in enumerate(GODs ,  101):
    print(numbers ,  ui)
