#  Write a Python program to find smallest and largest word in a given string.
str=input("enter the string")
list=str.split()
#print(list)
largest=0
large_word=''
smallest=len(list[1])
small_word=''

for i in list:
    if len(i)>largest:
        largest=len(i)
        large_word=i
        
    if len(i)<smallest:
        smallest=len(i)
        small_word=i
        
print("largest word is" +large_word+"of length",largest)
print("smallest word is" +small_word+"of length",smallest)