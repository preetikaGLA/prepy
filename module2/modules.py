'''
#3check/ set system path
import sys
print(sys.path)# sys.path variable has all path where python seaarch modules
#error     set PYTHONPATH=%PYTHONPATH%;C:\PerfLogs
if "C:\\My_Python_Lib" not in sys.path:
    sys.path.append("C:\\My_Python_Lib")

##2 import modules rename
#import prepy as pr
'''
'''
#1. In this exercise, you will need to print an alphabetically sorted list of all functions in the re module, which contain the word find
import re

# Your code goes here
find_members = []
for member in dir(re):
    if "find" in member:
        find_members.append(member)

print(sorted(find_members))
'''
'''
import urllib

a=urllib.urlopen('https://docs.python.org/2/tutorial/modules.html')
print(a)ERROR
'''
