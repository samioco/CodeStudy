#PBC13_AdvancedPythonModules03_PythonDebugger.py

print("""
Python Debugger
You've probably used a variety of print statements to try to find errors in your code. 
A better way of doing this is by using Python's built-in debugger module (pdb). 
The pdb module implements an interactive debugging environment for Python programs. 
It includes features to let you pause your program, look at the values of variables, 
and watch program execution step-by-step, so you can understand what your program 
actually does and find bugs in the logic.

This is a bit difficult to show since it requires creating an error on purpose, 
but hopefully this simple example illustrates the power of the pdb module. 
Note: Keep in mind it would be pretty unusual to use pdb in an iPython Notebook setting.

""")

import pdb

x = [1,3,4]
y = 2
z = 3
print("result = y + z. Printing: result")
result = y + z
print(result)

print("""
pdb.set_trace()

https://docs.python.org/3/library/pdb.html

q(uit)

h(elp) [command]

s(tep): Execute the current line, stop at the first possible occasion 
	(either in a function that is called or on the next line in the 
	current function).

n(ext): Continue execution until the next line in the current function 
	is reached or it returns. (The difference between next and step is 
	that step stops inside a called function, while next executes called 
	functions at (nearly) full speed, only stopping at the next line 
	in the current function.)
""")
pdb.set_trace()
result2 = y+x
print(result2)

