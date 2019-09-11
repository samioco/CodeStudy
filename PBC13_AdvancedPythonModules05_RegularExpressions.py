#PBC13_AdvancedPythonModules05_RegularExpressions.py

print("""
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
Now we've seen that re.search() will take the pattern, scan the text, 
and then return a Match object. If no pattern is found, None is returned. 
""")

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


print("""
Split with regular expressions
Let's see how we can split with the re syntax. This should look similar to 
how you used the split() method with strings.
""")


# Term to split on
split_term = '@'

phrase = 'What is the domain name of someone with the email: hello@gmail.com'

# Split the phrase
re.split(split_term,phrase)

