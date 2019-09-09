#PythonBootCamp_13_AdvancedPythonModules

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
print("Printing d['one'] (hasn't been declared):")
d['one']



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

