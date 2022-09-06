# Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
# Sample String : 'abc'
# Expected Result : 'abcing' 
# Sample String : 'string'
# Expected Result : 'stringly'

strings= input("enter the strings to add letters at the end of the strings")
n=len(strings)

if n>2:
    if strings[-3:]=='ing':
        strings+='ly'
    else:
        strings+='ing'

print(strings)