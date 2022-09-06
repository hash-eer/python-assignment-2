# Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
# Sample String : 'restart'
# Expected Result : 'resta$t'
strings=input("enter the strings to change its repeated first chracter")
char=strings[0]
strings=strings.replace(char,'$')  #replaces all the first character with $
strings=char + strings[1:] #adding first character to the string
print(strings)