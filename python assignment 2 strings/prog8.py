#  Write a Python function that takes a list of words and returns the length of the longest one. 

# str=input("enetr the strings to find the largest word")
# list=str.split()

list=[]
n=int(input("enetr the size of the list"))
for i in range(0,n):
    print("enter the words at index ",i)
    items=input()
    list.append(items)
print(list)
large=0
word=''

for i in list:
    if len(i)>large:
        large=len(i)
        word=i

print("largest word is",word)
print("its length is",large)