"""

Python List extend()
 -: The extend() method adds all the elements of an iterable (list, tuple, string etc.) to the end of the list.
  ** used to copy one list to another list .

The syntax of the extend() method is:

list1.extend(iterable)

"""
lt = ['a' , 'b' , 'c' , 'd']

lt1 = [1 , 2 , 3 , 4]

lt2 = ['e' , 'f']

lt.extend(lt2)
print(lt)

lt.extend(lt1)
print(lt)

"""
** Another way to extend list : - using ' + ' operator

"""
lt3 = [5,6]
print(" using plus operator " , lt2+lt3)

"""
** copy file using ' = ' operator
"""

lt4 = [100 , 200]

lt4 = lt1;
print(lt4)

lt5 = []
print(lt5+lt4)


"""

Python List count()
 -: The count() method returns the number of times the specified element appears in the list.
 LIKE - one time , two times , ..... so on

The syntax of the count() method is:

list.count(element)

"""

stmt = ['Honesty is best policy']

cnt = stmt.count('e')

print("count :: ",cnt)


stmt1 = ['Honesty is best policy' , 'a' , 'e' ,'i' , 'o' , 'u' , 'e']

cnt1 = stmt1.count('e')

print("count 1 :: ",cnt1)

#######################################
#logic

st = str(stmt)
print(st)


ltt = []
for x in st:
    ltt.append(x)
print(ltt)

print("logic count s :: ", ltt.count('s'))

alpha = []
for c in range(97 , 123):
    alpha.append(chr(c))
print(alpha)

"""
co = 0
for x in range(len(ltt)):
    if ltt[x] in alpha:
        co += 1
    else:
        pass

    print(co)

"""





"""

Python List insert()
  -: The list insert() method inserts an element to the list at the specified index.


The syntax of the insert() method is

list.insert(i, elem)

# vowel list
vowel = ['a', 'e', 'i', 'u']

# 'o' is inserted at index 3
# the position of 'o' will be 4th
vowel.insert(3, 'o')

print('Updated List:', vowel)
Output

Updated List: ['a', 'e', 'i', 'o', 'u']

"""



"""
Python List index()
The index() method returns the index of the specified element in the list.

The syntax of the list index() method is:

list.index(element, start, end)

Note: The index() method only returns the first occurrence of the matching element.


"""

in1 = ['a', 'e', 'i', 'o', 'u' , 'o']

print("indexing of o ",in1.index('o'))
print(in1.index('o' , 4))




"""

Python List remove()
  - : The remove() method removes the first matching element (which is passed as an argument) from the list.

NOTE : If a list contains duplicate elements, the remove() method only removes the first matching element.

The syntax of the remove() method is:

list.remove(element)

"""

rm = ['a', 'e', 'i', 'o', 'u' , 'o' , 'a' , 'o']

rm.remove('a')

print(rm)

rm.remove('o')

print(rm)
