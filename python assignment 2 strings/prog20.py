# Write a Python program to remove all consecutive duplicates of a given string.
# string=input("enter the consecutive string")
# tuple1=set(string)
# print(''.join(tuple1))

string=input("enter the consecutive string")
s1=''
i=0
for x in string:
    if string.index(x)==i:
        s1+=x
    i+=1
    
print(s1)
        