
dt = {'a' : 1 , 'b' : 2 , 'c' : [3,4,5]}

print(dt)

print(dt['c'])

# nother way

print(dt.get('b'))

dt['b'] = 100

dt['d'] = 20.02
print(dt)

# get vs [] for retrieving elements
my_dict = {'name': 'Jack', 'age': 26}

# Output: Jack
print(my_dict['name'])

# Output: 26
print(my_dict.get('age'))

# Trying to access keys which doesn't exist throws error
# Output None
print(my_dict.get('address')) # None

# KeyError
""" print(my_dict['address'])  # KeyError """



"""

We can remove a particular item in a dictionary by using the pop() method.
This method removes an item with the provided key and returns the value.

The popitem() method can be used to remove and return an arbitrary (key, value) item pair from the dictionary.
All the items can be removed at once, using the clear() method.

We can also use the del keyword to remove individual items or the entire dictionary itself.

"""

print(dt , "remove the d" , dt.pop('d') , dt)

print("using popitem() ", dt.popitem() , dt)

print("delete all items of dictionary :: clear()" , dt.clear())

print("delete the whole dictionary itself ' del ' ::  " , dt)

del dt

 #print(dt)


print("creating a new dictionary using fromkeys")

marks = {}.fromkeys(['math' , 'Hindi' , 'social science'] , 90)

print(marks)

print("items of dict ",marks.items())

print("keys of marks ",marks.keys())

print("values of marks  : ",marks.values())

print("\n", "\n" , "\n")

# dictionary comprehensive

sqr = {x : x*x for x in range(11)}

print("square of sqr-dict" , sqr)

"""

neasted dictionary

"""

Ndt = {1 : {'name' : 'Om namh shivay' , 'location' : 'every where'} ,
       2: {'name' : 'mata rani_shakti' , 'location': 'every where'}}

print('\n' , '\n')
print(Ndt)

print(Ndt[1])
print(Ndt[1]['name'])
print(Ndt[2]['name'])

Ndt[3] = {'name' : 'Krishan g'}

print(Ndt)

Ndt[3]['quality'] = ' mitra mahan'

print(Ndt)

print(Ndt.items())

for key , val in Ndt.items():
    print("keys are : " ,key)
    print("values are : " ,val)
    print()

    print("keys : ",key)
    for k in val:
        print(k , val[k])
