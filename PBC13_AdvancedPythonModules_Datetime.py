#PBC13_AdvancedPythonModules_Datetime.py

print('''
#PBC13_AdvancedPythonModules_Datetime.py
datetime
Python has the datetime module to help deal with timestamps in your code. 
Time values are represented with the time class. Times have attributes for 
hour, minute, second, and microsecond. They can also include time zone 
information. The arguments to initialize a time instance are optional, 
but the default of 0 is unlikely to be what you want.

time
Let's take a look at how we can extract time information from the datetime 
module. We can create a timestamp by specifying 
datetime.time(hour,minute,second,microsecond)
''')



import datetime
print("t = datetime.time(4,20,1)")
t = datetime.time(4,20,1)
print(t)
print(t.minute)
print(t.microsecond)
datetime.time