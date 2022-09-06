# #Write a Python program to count the number of characters (character frequency) in a string. 
# Sample String : google.com'
# Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}


strings=input("enter the srings to calculate its character occurances:")
l=list(strings)  #converting string to list
#print(l)

frequency =[l.count(i) for i in l] # frequency will store list of occurances of each alphabet
#print(frequency)
d=dict(zip(l,frequency)) # this will convet number of occuraces with occurance with character
print(d)



