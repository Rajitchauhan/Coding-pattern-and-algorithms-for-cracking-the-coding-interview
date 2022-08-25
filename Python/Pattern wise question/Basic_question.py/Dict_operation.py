dt = {'a':1 , 'b':2 , 'c':3 , 'd': 4}

DT = dict({'a':1, 'b':2})
DT =  dict([(1  , 'cs') ,( 2 , 'ce') , (3 , 'ee')])

print(dt)
print(DT)
print()
# accessing element
for i in dt:
    print("using '{}' only :: " , dt)

for i in DT:
    print("using dict :: ",DT)


DT[4] = "me"
print("after adding :: ",DT)
DT[4] = "diploma"
print("after adding :: ",DT)

for i in range(5):
    d={}
    d[i] = i
    print(d)
print(d)

d['value_set'] = 1,2,3,4,5
print("add value  set 1,2,3,4,5",d)
#print("dict does not allow indexing ",dt[0])
print("print value with the help of key")
print("dt[key]  it return value :: ",dt['a'])
print("Return all  keys from dictionary")
for k in dt.keys():
    print("key are ",k)

print("Return all values from dictionary")
for  val in dt.values():
    print("value are ",val)
print("using zip")
for key , val in zip(dt.keys() , dt.values()):
    print("using zip ::" , key , val , key)

for i , key in enumerate(dt.keys()):
    print(F"enumerate :: ", i , key)

for i in dt:
    print("iterate 'i' and its print key ::",i)

for i in dt:
    print("iterate 'dt[i]' and print value ::" , dt[i])

print()
print("accessing key using value")
print()

dictionary = {'a': 2 , 'b':1 , 'c':1 , 'd':3}
mx = max(dictionary.values())
print(f'maximum value of dictionary ::  {mx}')
key = [k for k , val in dictionary.items() if val == mx]
if key:
    print("Key from dictionary using its value ::  ",key[0])
