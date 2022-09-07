#  Write a Python program to find smallest and largest word in a given string.
str=input("enter the string")
list=str.split()
#print(list)
largest=0
large_word=[]
smallest=len(list[1])
small_word=[]

for i in list:
    if len(i)>largest:
        largest=len(i)
        large_word.append(i)
        
    if len(i)<smallest:
        smallest=len(i)
        small_word.append(i)
        
for i in list:
    if len(i)==largest:
        large_word.append(i)
    
    if len(i)==smallest:
        small_word.append(i)
        
print("largest word is" ,large_word)
print("smallest word is", small_word)