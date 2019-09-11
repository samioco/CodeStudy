#PBC13_AdvancedPythonModules05_RegularExpressions.py

print("""------------------------------------------------------------
Regular Expressions
Regular expressions are text-matching patterns described with 
a formal syntax. You'll often hear regular expressions referred 
to as 'regex' or 'regexp' in conversation. Regular expressions 
can include a variety of rules, from finding repetition, 
to text-matching, and much more. As you advance in Python you'll
see that a lot of your parsing problems can be solved with regular 
expressions (they're also a common interview question!).

If you're familiar with Perl, you'll notice that the syntax for 
regular expressions are very similar in Python. We will be using 
the re module with Python for this lecture.
""")

print("""
------------------------------------------------------------

re.search(pattern,text): 
Searching for Patterns in Text
One of the most common uses for the re module is for finding 
patterns in text. Let's do a quick example of using the search 
method in the re module to find some text:
""")

import re

print("""
# List of patterns to search for
patterns = ['term1', 'term2']

# Text to parse
text = 'This is a string with term1, but it does not have the other term.'

for pattern in patterns:
    print('Searching for "%s" in:\n "%s"\n' %(pattern,text))
    
    #Check for match
    if re.search(pattern,text):
        print('Match was found. \n')
    else:
        print('No Match was found.\n')

""")

# List of patterns to search for
patterns = ['term1', 'term2']

# Text to parse
text = 'This is a string with term1, but it does not have the other term.'

for pattern in patterns:
    print('Searching for "%s" in:\n "%s"' %(pattern,text))
    
    #Check for match
    if re.search(pattern,text):
        print(f'Match found for pattern: {pattern} \n')
    else:
        print(f'Match NOT found for pattern: {pattern} \n')


print("""
match = re.search(patterns[0],text)
print(type(match))
""")
match = re.search(patterns[0],text)
print(type(match))




print("""
------------------------------------------------------------

match.start(), match.end()
Now we've seen that re.search() will take the pattern, scan the text, 
and then return a Match object. If no pattern is found, None is returned.""")

print("""
# List of patterns to search for
pattern = 'term1'
# Text to parse
text = 'This is a string with term1, but it does not have the other term.'
match = re.search(pattern,text)
print(type(match))
""")

# List of patterns to search for
pattern = 'term1'
# Text to parse
text = 'This is a string with term1, but it does not have the other term.'
match = re.search(pattern,text)
print(type(match))


print("""
_sre.SRE_Match
This Match object returned by the search() method is more than just a Boolean 
or None, it contains information about the match, including the original 
input string, the regular expression that was used, and the location of the 
match. Let's see the methods we can use on the match object:
""")

print("print(match.start())")
print(match.start())

print("print(match.end())")
print(match.end())
print("")

print("""
------------------------------------------------------------

re.split(pattern,text):
Split with regular expressions:
Let's see how we can split with the re syntax. This should look similar to 
how you used the split() method with strings. The term to split is removed.
""")


# Term to split on
print("""Splitting on a term using regular expressions:
phrase = 'What is the domain name of someone with the email: hello@gmail.com'
split_term = '@'
print(re.split(split_term,phrase)):
""")
phrase = 'How do you split an email address from it\'s domain: hello@gmail.com'
split_term = '@'
# Split the phrase
print(re.split(split_term,phrase))


print("""
------------------------------------------------------------

re.findall()
Finding all instances of a pattern
You can use re.findall() to find all the instances of a pattern in a string. 
For example:
#Returns a list of all matches (the length of which = # of matches)
re.findall('match','Here is one match, here is another match')""")
print(re.findall('match','Here is one match, here is another match'))

print("""
------------------------------------------------------------

re Pattern Syntax
This will be the bulk of this lecture on using re with Python. 
Regular expressions support a huge variety of patterns beyond 
just simply finding where a single string occurred.

We can use metacharacters along with re to find specific types of patterns.

Since we will be testing multiple re syntax forms, let's create a 
function that will print out results given a list of various 
regular expressions and a phrase to parse:

def multi_re_find(patterns,phrase):
    '''
    Takes in a list of regex patterns
    Prints a list of all matches
    '''
    for pattern in patterns:
        print('Searching the phrase using the re check: %r' %(pattern))
        print(re.findall(pattern,phrase))
        print('\n')
""")


def multi_re_find(patterns,phrase):
    '''
    Takes in a list of regex patterns
    Prints a list of all matches
    '''
    for pattern in patterns:
        print('Searching the phrase using the re check: %r' %(pattern))
        print(re.findall(pattern,phrase))
        print('\n')


