#  Write a Python function that takes a list of words and returns the length of the longest one. 

str=input("enetr the strings to find the largest word")
list=str.split()
print(list)
large=0
word=''

for i in list:
    if len(i)>large:
        large=len(i)
        word=i

print("largest word is",word)
print("its length is",large)