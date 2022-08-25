"""
Collections in python are basically container data types, namely lists, sets, tuples, dictionary. They have different characteristics based on the declaration and the usage.

A list is declared in square brackets, it is mutable, stores duplicate values and elements can be accessed using indexes.

A tuple is ordered and immutable in nature, although duplicate entries can be there inside a tuple.

A set is unordered and declared in square brackets. It is not indexed and does not have duplicate entries as well.

A dictionary has key value pairs and is mutable in nature. We use square brackets to declare a dictionary.
"""
from collections import namedtuple

a = namedtuple('courses' , 'name , tech')
s = a('data science' , 'python')
print(s)
#courses(name='data science', tech='python')

from collections import deque

a = ['S' , 'h' ,'i' , 'v']

s = deque(a)
print(s)
s.appendleft('Sati')
print(s)

from collections import Counter

dup = ['a' , 's' , 's' , 'd' , 'a' , 's' , 'd' , 'e']

c = Counter(dup)

print(c)
print(list(c.elements()))
sub = {'a' : 1 , 'd' : 1}


############################################################
from collections import defaultdict
d = defaultdict(list)
d['python'].append("awesome")
d['something-else'].append("not relevant")
d['python'].append("language")
for i in d.items():
    print i