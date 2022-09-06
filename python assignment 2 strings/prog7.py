# Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
# Sample String : 'The lyrics is not that poor!'
# 'The lyrics is poor!'
# Expected Result : 'The lyrics is good!'
# 'The lyrics is poor!'

strings= input("enter the strings to replace not and poor from the string")
 
a =strings.find('not') #finding position of not
print(a)
b=strings.find('poor') #finding position of poor
print(b)


if a>=0 and b>=0:
    
    strings=strings.replace(strings[a:(b+4)],'good')
    
print(strings)

