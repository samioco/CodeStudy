#PBC13_AdvancedPythonModules01_CollectionsModule.py

#CollectionsModule
print('''Collections Module
The collections module is a built-in module that implements specialized container data types 
providing alternatives to Python’s general purpose built-in containers. 
We've already gone over the basics: dict, list, set, and tuple.

Now we'll learn about the alternatives that the collections module provides.

Counter
Counter is a dict subclass which helps count hashable objects. 
Inside of it elements are stored as dictionary keys and the counts of the objects are stored as the value.

Let's see how it can be used:
''')

from collections import Counter
l1=[1,1,1,1,1,2,2,2,2,2,2,3,3,4,4,4,4,5,5,5,5,5,5,5]
print(f"list l1: {l1}")
print("Counter(l1):")
Counter(l1)
#Counter({1: 6, 2: 6, 3: 4, 12: 1, 21: 1, 32: 1, 223: 1})
Counter('aabsbsbsbhshhbbsbs')
#Counter({'a': 2, 'b': 7, 'h': 3, 's': 6})
s = 'How many times does each word show up in this sentence word times each each word'
words = s.split()
Counter(words)

#Methoeds with Counter()
c = Counter(words)
c.most_common(2)

print('''
# Methods with Counter()
c = Counter(words)

c.most_common(2)
Out[5]:
[('each', 3), ('word', 3)]
Common patterns when using the Counter() object
sum(c.values())                 # total of all counts
c.clear()                       # reset all counts
list(c)                         # list unique elements
set(c)                          # convert to a set
dict(c)                         # convert to a regular dictionary
c.items()                       # convert to a list of (elem, cnt) pairs
Counter(dict(list_of_pairs))    # convert from a list of (elem, cnt) pairs
c.most_common()[:-n-1:-1]       # n least common elements
c += Counter()                  # remove zero and negative counts

''')



#defaultdict
print('''
defaultdict
defaultdict is a dictionary-like object which provides all methods provided by a dictionary 
but takes a first argument (default_factory) as a default data type for the dictionary. 
Using defaultdict is faster than doing the same using dict.set_default method.

A defaultdict will never raise a KeyError. 
Any key that does not exist gets the value returned by the default factory.

''')


d = {}
#d['one']
#produces a KeyError

from collections import defaultdict

#for item in d: print(item)
d = defaultdict(lambda:0)
print("Printing d['one'] (hasn't been declared):",d['one'],"\n")


print('Normal dictionary:')
d = {}
d['d'] = 'D'
d['c'] = 'C'
d['b'] = 'B'
d['a'] = 'A'
d['e'] = 'E'
for k, v in d.items():
    print(k, v)
'''
Normal dictionary:
a A
b B
c C
d D
e E
'''

#An Ordered Dictionary:
from collections import OrderedDict
print("""

OrderedDict
An OrderedDict is a dictionary subclass that remembers the order in which its contents are added.
""")
print('OrderedDict:')

d = OrderedDict()
d['d'] = 'D'
d['c'] = 'C'
d['b'] = 'B'
d['a'] = 'A'
d['e'] = 'E'

for k, v in d.items():
    print(k, v)


'''
OrderedDict:
a A
b B
c C
d D
e E
'''

print("""
Equality with an Ordered Dictionary
A regular dict looks at its contents when testing for equality. An OrderedDict also considers the order the items were added.
A normal Dictionary:
d1 = {}
d1['a'] = 'A'
d1['b'] = 'B'
d2 = {}
d2['b'] = 'B'
d2['a'] = 'A'

""")

d1 = {}
d1['a'] = 'A'
d1['b'] = 'B'

d2 = {}
d2['b'] = 'B'
d2['a'] = 'A'

print("Dictionaries are equal? (Normal)")
print(d1==d2)

'''
Dictionaries are equal?
True
An Ordered Dictionary:
'''

print('\nDictionaries are equal? (Ordered)')

d1 = OrderedDict()
d1['a'] = 'A'
d1['b'] = 'B'
d2 = OrderedDict()
d2['b'] = 'B'
d2['a'] = 'A'

print(d1==d2)
''' Will print:
Dictionaries are equal?
False
'''
print("\n\n")

#namedtuple
print("namedtuple:\n")
t = (12,13,14)
t[0]
'''
12
For simple use cases, this is usually enough. 
On the other hand, remembering which index should 
be used for each value can lead to errors, 
especially if the tuple has a lot of fields and 
is constructed far from where it is used. 
A namedtuple assigns names, as well as the 
numerical index, to each member.

Each kind of namedtuple is represented by its own class, 
created by using the namedtuple() factory function. The 
arguments are the name of the new class and a string 
containing the names of the elements.

You can basically think of namedtuples as a very quick 
way of creating a new object/class type with some attribute 
fields. For example:
'''
from collections import namedtuple

print("""
Assigning:
Dog = namedtuple('Dog','age breed name')
sam = Dog(age=2,breed='Lab',name='Sammy')
frank = Dog(age=2,breed='Shepard',name="Frankie")
""")

Dog = namedtuple('Dog','age breed name')
sam = Dog(age=2,breed='Lab',name='Sammy')
frank = Dog(age=2,breed='Shepard',name="Frankie")

'''
We construct the namedtuple by first passing the object 
type name (Dog) and then passing a string with the 
variety of fields as a string with spaces between the 
field names. We can then call on the various attributes:
'''
print("Calling: 'sam'")
sam
#Dog(age=2, breed='Lab', name='Sammy')
print("Calling: 'sam.age'")
sam.age
#2
print("Calling: 'sam.breed'")
sam.breed
#'Lab'
print("Calling: 'sam[0]'")
sam[0]
2

print("""
Assigning:
Cat = namedtuple('Cat','fur claws name')
c = Cat(fur='Fuzzy',claws=False,name='Kitty')
""")
Cat = namedtuple('Cat','fur claws name')
c = Cat(fur='Fuzzy',claws=False,name='Kitty')

print("Calling: 'c'")
c
print("Calling: 'c.name'")
c.name
print("Calling: 'c[2]'")
c[2]
print("Calling: 'c[1]'")
c[1]

