# Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters.
str=input("enter the strings")
count=0
for i in str[:5]:
    if i.upper()==i:
        count+=1
        
if count>2:
    print("yes first 2 character of strings is upper case:",str.upper())
else:
    print("first 2 charcter of the string is not a upper:",str)
        