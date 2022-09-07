#  Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically). 
# Sample Words : red, white, black, red, green, black
# Expected Result : black, green, red, white

strings=input("enter the words with the comma seperated").split(',')
print(strings)
#print(set(strings))
a=list(set(strings))
a.sort()
list_to_str=','.join(map(str,a))
print((list_to_str))