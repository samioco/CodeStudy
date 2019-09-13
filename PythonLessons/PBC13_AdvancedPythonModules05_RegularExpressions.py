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


print("""

Repetition Syntax
There are five ways to express repetition in a pattern:

. A pattern followed by the meta-character * is repeated zero or more times.
. Replace the * with + and the pattern must appear at least once.
. Using ? means the pattern appears zero or one time.
. For a specific number of occurrences, use {m} after the pattern, where m is 
	replaced with the number of times the pattern should repeat.
. Use {m,n} where m is the minimum number of repetitions and n is the maximum. 
	Leaving out n {m,} means the value appears at least m times, with no maximum.

Now we will see an example of each of these using our multi_re_find function:

test_phrase = 'sdsd..sssddd...sdddsddd...dsds...dsssss...sdddd'

test_patterns = [ 'sd*',     # s followed by zero or more d's
                'sd+',          # s followed by one or more d's
                'sd?',          # s followed by zero or one d's
                'sd{3}',        # s followed by three d's
                'sd{2,3}',      # s followed by two to three d's
                ]
multi_re_find(test_patterns,test_phrase)
""")

test_phrase = 'sdsd..sssddd...sdddsddd...dsds...dsssss...sdddd'

test_patterns = [ 'sd*',     # s followed by zero or more d's
                'sd+',          # s followed by one or more d's
                'sd?',          # s followed by zero or one d's
                'sd{3}',        # s followed by three d's
                'sd{2,3}',      # s followed by two to three d's
                ]

multi_re_find(test_patterns,test_phrase)

print("""
------------------------------------------------------------

Character Sets []
Character sets are used when you wish to match any one of a group 
of characters at a point in the input. Brackets are used to construct 
character set inputs. For example: the input [ab] searches for occurrences 
of either a or b. Let's see some examples:

test_phrase = 'sdsd..sssddd...sdddsddd...dsds...dsssss...sdddd'
test_patterns = ['[sd]',    # either s or d
                's[sd]+']   # s followed by one or more s or d
multi_re_find(test_patterns,test_phrase)
""")

test_phrase = 'sdsd..sssddd...sdddsddd...dsds...dsssss...sdddd'
test_patterns = ['[sd]',    # either s or d
                's[sd]+']   # s followed by one or more s or d
multi_re_find(test_patterns,test_phrase)
"""Output:
Searching the phrase using the re check: '[sd]'
['s', 'd', 's', 'd', 's', 's', 's', 'd', 'd', 'd', 's', 'd', 'd', 'd', 's', 'd', 
'd', 'd', 'd', 's', 'd', 's', 'd', 's', 's', 's', 's', 's', 's', 'd', 'd', 'd', 'd']

Searching the phrase using the re check: 's[sd]+'
['sdsd', 'sssddd', 'sdddsddd', 'sds', 'sssss', 'sdddd']
"""



print("""
It makes sense that the first input [sd] returns every instance of s or d. 
Also, the second input s[sd]+ returns any full strings that begin with an 
s and continue with s or d characters until another character is reached.

Exclusion
We can use ^ to exclude terms by incorporating it into the bracket syntax 
notation. For example: [^...] will match any single character not in the 
brackets. Let's see some examples:

test_phrase = 'This is a string! But it has punctuation. How can we remove it?'

Use [^!.? ] to check for matches that are not a !,.,?, or space. Add a + to 
check that the match appears at least once. This basically translates into 
finding the words.

re.findall('[^!.? ]+',test_phrase)
""")
test_phrase = 'This is a string! But it has punctuation. How can we remove it?'
print(re.findall('[^!.? ]+',test_phrase))

'''Output:
['This', 'is', 'a', 'string', 'But', 'it', 'has', 'punctuation', 'How', 'can', 
'we', 'remove', 'it']
'''

print("""
------------------------------------------------------------

Character Ranges
As character sets grow larger, typing every character that should (or should not) 
match could become very tedious. A more compact format using character ranges lets 
you define a character set to include all of the contiguous characters between a 
start and stop point. The format used is [start-end].

Common use cases are to search for a specific range of letters in the alphabet. 
For instance, [a-f] would return matches with any occurrence of letters between a and f.

Let's walk through some examples:
test_phrase = 'This is an example sentence. Lets see if we can find some letters.'

test_patterns=['[a-z]+',      # sequences of lower case letters
               '[A-Z]+',      # sequences of upper case letters
               '[a-zA-Z]+',   # sequences of lower or upper case letters
               '[A-Z][a-z]+'] # one upper case letter followed by lower case letters
                
multi_re_find(test_patterns,test_phrase)
""")
test_phrase = 'This is an example sentence. Lets see if we can find some letters.'
test_patterns=['[a-z]+',      # sequences of lower case letters
               '[A-Z]+',      # sequences of upper case letters
               '[a-zA-Z]+',   # sequences of lower or upper case letters
               '[A-Z][a-z]+'] # one upper case letter followed by lower case letters
               
multi_re_find(test_patterns,test_phrase)
"""
Searching the phrase using the re check: '[a-z]+'
['his', 'is', 'an', 'example', 'sentence', 'ets', 'see', 'if', 'we', 'can', 'find', 
'some', 'letters']

Searching the phrase using the re check: '[A-Z]+'
['T', 'L']

Searching the phrase using the re check: '[a-zA-Z]+'
['This', 'is', 'an', 'example', 'sentence', 'Lets', 'see', 'if', 'we', 'can', 'find', 
'some', 'letters']

Searching the phrase using the re check: '[A-Z][a-z]+'
['This', 'Lets']
"""


print("""
------------------------------------------------------------

Escape Codes
You can use special escape codes to find specific types of patterns in your data, 
such as digits, non-digits, whitespace, and more. For example:

Code	Meaning
\d	a digit
\D	a non-digit
\s	whitespace (tab, space, newline, etc.)
\S	non-whitespace
\w	alphanumeric
\W	non-alphanumeric
Escapes are indicated by prefixing the character with a backslash \. Unfortunately, 
a backslash must itself be escaped in normal Python strings, and that results in 
expressions that are difficult to read. Using raw strings, created by prefixing 
the literal value with r, eliminates this problem and maintains readability.

Personally, I think this use of r to escape a backslash is probably one of the 
things that block someone who is not familiar with regex in Python from being 
able to read regex code at first. Hopefully after seeing these examples this 
syntax will become clear.

test_phrase = 'This is a string with some numbers 1233 and a symbol #hashtag'
test_patterns=[ r'\d+', # sequence of digits
                r'\D+', # sequence of non-digits
                r'\s+', # sequence of whitespace
                r'\S+', # sequence of non-whitespace
                r'\w+', # alphanumeric characters
                r'\W+', # non-alphanumeric
                ]
multi_re_find(test_patterns,test_phrase)
""")

test_phrase = 'This is a string with some numbers 1233 and a symbol #hashtag'
test_patterns=[ r'\d+', # sequence of digits
                r'\D+', # sequence of non-digits
                r'\s+', # sequence of whitespace
                r'\S+', # sequence of non-whitespace
                r'\w+', # alphanumeric characters
                r'\W+', # non-alphanumeric
                ]
multi_re_find(test_patterns,test_phrase)

"""Output:
Searching the phrase using the re check: '\\d+'
['1233']

Searching the phrase using the re check: '\\D+'
['This is a string with some numbers ', ' and a symbol #hashtag']

Searching the phrase using the re check: '\\s+'
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

Searching the phrase using the re check: '\\S+'
['This', 'is', 'a', 'string', 'with', 'some', 'numbers', '1233', 'and', 
'a', 'symbol', '#hashtag']

Searching the phrase using the re check: '\\w+'
['This', 'is', 'a', 'string', 'with', 'some', 'numbers', '1233', 'and', 
'a', 'symbol', 'hashtag']

Searching the phrase using the re check: '\\W+'
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' #']
"""

print("""
------------------------------------------------------------

Conclusion of Udemy.com Regex
You should now have a solid understanding of how to use the regular expression 
module in Python. There are a ton of more special character instances, but 
it would be unreasonable to go through every single use case. Instead take 
a look at the full documentation if you ever need to look up a particular pattern.

You can also check out the nice summary tables at this source.

Good job!

------------------------------------------------------------
""")


print("""
------------------------------------------------------------

http://www.tutorialspoint.com/python/python_reg_expressions.htm

The match Function
This function attempts to match RE pattern to string with optional flags.
Here is the syntax for this function −
re.match(pattern, string, flags=0)
Here is the description of the parameters −

Parameter & Description
pattern: This is the regular expression to be matched.

string: This is the string, which would be searched to match the pattern 
at the beginning of string.

flags: You can specify different flags using bitwise OR (|). These are modifiers, 
which are listed in the table below.

The re.match function returns a match object on success, None on failure. 
We usegroup(num) or groups() function of match object to get matched expression.

Match Object Method & Description
group(num=0)
This method returns entire match (or specific subgroup num)

groups()
This method returns all matching subgroups in a tuple (empty if there weren't any)

Regular Expression Modifiers: Option Flags
Regular expression literals may include an optional modifier to control various 
aspects of matching. The modifiers are specified as an optional flag. 
You can provide multiple modifiers using exclusive OR (|), as shown previously 
and may be represented by one of these −
Modifier & Description

re.I
Performs case-insensitive matching.

re.L
Interprets words according to the current locale. This interpretation affects 
the alphabetic group (\w and \W), as well as word boundary behavior(\b and \B).

re.M
Makes $ match the end of a line (not just the end of the string) and makes ^ match 
the start of any line (not just the start of the string).

re.S
Makes a period (dot) match any character, including a newline.
	
re.U
Interprets letters according to the Unicode character set. This flag affects 
the behavior of \w, \W, \b, \B.

re.X
Permits "cuter" regular expression syntax. It ignores whitespace 
(except inside a set [] or when escaped by a backslash) and treats unescaped # 
as a comment marker.

""")

print("""
------------------------------------------------------------

import re
line = "Cats are smarter than dogs"
matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)

if matchObj:
   print "matchObj.group() : ", matchObj.group()
   print "matchObj.group(1) : ", matchObj.group(1)
   print "matchObj.group(2) : ", matchObj.group(2)
else:
   print "No match!!"

When the above code is executed, it produces following result:
matchObj.group() :  Cats are smarter than dogs
matchObj.group(1) :  Cats
matchObj.group(2) :  smarter

""")
import re
line = "Cats are smarter than dogs"
matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)

if matchObj:
   print("matchObj.group() : ", matchObj.group())
   print("matchObj.group(1) : ", matchObj.group(1))
   print("matchObj.group(2) : ", matchObj.group(2))
else:
   print("No match!!")


print("""
------------------------------------------------------------
The search Function:
This function searches for first occurrence of RE pattern within string with optional flags.

Here is the syntax for this function:
re.search(pattern, string, flags=0)

Here is the description of the parameters:
Parameter & Description
pattern: This is the regular expression to be matched.
string: This is the string, which would be searched to match 
the pattern anywhere in the string.
flags: You can specify different flags using bitwise OR (|). 
These are modifiers, which are listed in the table below.

The re.search function returns a match object on success, none on failure. 
We use group(num) or groups() function of match object to get matched expression.


Match Object Methods & Description
group(num=0): This method returns entire match (or specific subgroup num)

groups()

This method returns all matching subgroups in a tuple (empty if there weren't any)

Example:
import re
line = "Cats are smarter than dogs";
searchObj = re.search( r'(.*) are (.*?) .*', line, re.M|re.I)
if searchObj:
   print "searchObj.group() : ", searchObj.group()
   print "searchObj.group(1) : ", searchObj.group(1)
   print "searchObj.group(2) : ", searchObj.group(2)
else:
   print "Nothing found!!"
When the above code is executed, it produces following result −

searchObj.group() :  Cats are smarter than dogs
searchObj.group(1) :  Cats
searchObj.group(2) :  smarter
""")

import re

line = "Cats are smarter than dogs";
searchObj = re.search( r'(.*) are (.*?) .*', line, re.M|re.I)
if searchObj:
   print("searchObj.group() : ", searchObj.group())
   print("searchObj.group(1) : ", searchObj.group(1))
   print("searchObj.group(2) : ", searchObj.group(2))
else:
   print("Nothing found!!")

print("""
------------------------------------------------------------
Matching Versus Searching
Python offers two different primitive operations based on regular expressions: 
match checks for a match only at the beginning of the string, while search checks 
for a match anywhere in the string (this is what Perl does by default).

Example:
import re
line = "Cats are smarter than dogs";
matchObj = re.match( r'dogs', line, re.M|re.I)
if matchObj:
   print "match --> matchObj.group() : ", matchObj.group()
else:
   print "No match!!"

searchObj = re.search( r'dogs', line, re.M|re.I)
if searchObj:
   print "search --> searchObj.group() : ", searchObj.group()
else:
   print "Nothing found!!"

When the above code is executed, it produces the following result −
No match!!
search --> matchObj.group() :  dogs

""")
import re
line = "Cats are smarter than dogs";
matchObj = re.match( r'dogs', line, re.M|re.I)
if matchObj:
   print("match --> matchObj.group() : ", matchObj.group())
else:
   print("No match!!")

searchObj = re.search( r'dogs', line, re.M|re.I)
if searchObj:
   print("search --> searchObj.group() : ", searchObj.group())
else:
   print("Nothing found!!")



print("""
------------------------------------------------------------
Search and Replace:P
One of the most important re methods that use regular expressions is sub.

Syntax
re.sub(pattern, repl, string, max=0)
This method replaces all occurrences of the RE pattern in string with repl, 
substituting all occurrences unless max provided. This method returns modified string.

Example:
import re
phone = "2004-959-559 # This is Phone Number"
# Delete Python-style comments
num = re.sub(r'#.*$', "", phone)
print "Phone Num : ", num

# Remove anything other than digits
num = re.sub(r'\D', "", phone)    
print "Phone Num : ", num
#When the above code is executed, it produces the following result −

Phone Num :  2004-959-559
Phone Num :  2004959559
""")
import re
phone = "2004-959-559 # This is Phone Number"
# Delete Python-style comments
num = re.sub(r'#.*$', "", phone)
print("Phone Num : ", num)

# Remove anything other than digits
num = re.sub(r'\D', "", phone)    
print("Phone Num : ", num)

print("""
------------------------------------------------------------
------------------------------------------------------------
Regular Expression Patterns
Except for control characters, (+ ? . * ^ $ ( ) [ ] { } | \), 
all characters match themselves. You can escape a control character 
by preceding it with a backslash.

Following table lists the regular expression syntax that is available in Python −
Pattern & Description

^
Matches beginning of line.	

$
Matches end of line.	

.
Matches any single character except newline. 
Using m option allows it to match newline as well.

	
[...]
Matches any single character in brackets.

	
[^...]
Matches any single character not in brackets

	
re*
Matches 0 or more occurrences of preceding expression.

	
re+
Matches 1 or more occurrence of preceding expression.

	
re?
Matches 0 or 1 occurrence of preceding expression.

	
re{ n}
Matches exactly n number of occurrences of preceding expression.

	
re{ n,}
Matches n or more occurrences of preceding expression.

	
re{ n, m}
Matches at least n and at most m occurrences of preceding expression.

	
a| b
Matches either a or b.

	
(re)
Groups regular expressions and remembers matched text.

	
(?imx)
Temporarily toggles on i, m, or x options within a regular expression. 
If in parentheses, only that area is affected.

	
(?-imx)
Temporarily toggles off i, m, or x options within a regular expression. 
If in parentheses, only that area is affected.

	
(?: re)
Groups regular expressions without remembering matched text.

	
(?imx: re)
Temporarily toggles on i, m, or x options within parentheses.

	
(?-imx: re)
Temporarily toggles off i, m, or x options within parentheses.

	
(?#...)
Comment.

	
(?= re)
Specifies position using a pattern. Doesn't have a range.

	
(?! re)
Specifies position using pattern negation. Doesn't have a range.

	
(?> re)
Matches independent pattern without backtracking.

	
\w
Matches word characters.

	
\W
Matches nonword characters.

	
\s
Matches whitespace. Equivalent to [\t\n\r\f].

	
\S
Matches nonwhitespace.

	
\d
Matches digits. Equivalent to [0-9].

	
\D
Matches nondigits.

	
\A
Matches beginning of string.

	
\Z
Matches end of string. If a newline exists, it matches just before newline.

	
\z
Matches end of string.

	
\G
Matches point where last match finished.

	
\b
Matches word boundaries when outside brackets. 
Matches backspace (0x08) when inside brackets.

	
\B
Matches nonword boundaries.

	
\n, \t, etc.
Matches newlines, carriage returns, tabs, etc.

	
\1...\9
Matches nth grouped subexpression.

	
\10
Matches nth grouped subexpression if it matched already. 
Otherwise refers to the octal representation of a character code.

""")

print("""
------------------------------------------------------------
------------------------------------------------------------

Regular Expression Examples
Literal characters
Example & Description
python

Match "python".

Character classes
Example & Description
[Pp]ython
Match "Python" or "python"

rub[ye]
Match "ruby" or "rube"

[aeiou]
Match any one lowercase vowel

[0-9]
Match any digit; same as [0123456789]

[a-z]
Match any lowercase ASCII letter

[A-Z]
Match any uppercase ASCII letter

[a-zA-Z0-9]
Match any of the above

[^aeiou]
Match anything other than a lowercase vowel

[^0-9]
Match anything other than a digit

------------------------------------------------------------
------------------------------------------------------------

Special Character Classes
Example & Description
.
Match any character except newline

\d
Match a digit: [0-9]

\D
Match a nondigit: [^0-9]

\s
Match a whitespace character: [ \t\r\n\f]

\S
Match nonwhitespace: [^ \t\r\n\f]

\w
Match a single word character: [A-Za-z0-9_]

\W
Match a nonword character: [^A-Za-z0-9_]

------------------------------------------------------------
------------------------------------------------------------

Repetition Cases
Example & Description
ruby?
Match "rub" or "ruby": the y is optional

ruby*
Match "rub" plus 0 or more y's

ruby+
Match "rub" plus 1 or more y's

\d{3}
Match exactly 3 digits

\d{3,}
Match 3 or more digits

\d{3,5}
Match 3, 4, or 5 digits

------------------------------------------------------------
------------------------------------------------------------

Nongreedy repetition
This matches the smallest number of repetitions −

Example & Description	
<.*>
Greedy repetition: matches "<python>perl>"

<.*?>
Nongreedy: matches "<python>" in "<python>perl>"

------------------------------------------------------------
------------------------------------------------------------

Grouping with Parentheses
Example & Description
\D\d+
No group: + repeats \d	

(\D\d)+
Grouped: + repeats \D\d pair
	
([Pp]ython(, )?)+
Match "Python", "Python, python, python", etc.

------------------------------------------------------------
------------------------------------------------------------

Backreferences
This matches a previously matched group again −

Sr.No.	Example & Description
([Pp])ython&\1ails

Match python&pails or Python&Pails

(['"])[^\1]*\1

Single or double-quoted string. 
\1 matches whatever the 1st group matched. 
\2 matches whatever the 2nd group matched, etc.

------------------------------------------------------------
------------------------------------------------------------

Alternatives
Example & Description
python|perl
Match "python" or "perl"
	
rub(y|le))
Match "ruby" or "ruble"

Python(!+|\?)
"Python" followed by one or more ! or one ?

------------------------------------------------------------
------------------------------------------------------------

Anchors
This needs to specify match position.

Example & Description
^Python
Match "Python" at the start of a string or internal line

Python$
Match "Python" at the end of a string or line

\APython
Match "Python" at the start of a string

Python\Z
Match "Python" at the end of a string

\bPython\b
Match "Python" at a word boundary

\brub\B
\B is nonword boundary: match "rub" in "rube" and "ruby" but not alone

Python(?=!)
Match "Python", if followed by an exclamation point.

Python(?!!)
Match "Python", if not followed by an exclamation point.

------------------------------------------------------------
------------------------------------------------------------

Special Syntax with Parentheses
Example & Description

R(?#comment)
Matches "R". All the rest is a comment


R(?i)uby
Case-insensitive while matching "uby"


R(?i:uby)
Same as above


rub(?:y|le))
Group only without creating \1 backreference

------------------------------------------------------------
------------------------------------------------------------
""")
