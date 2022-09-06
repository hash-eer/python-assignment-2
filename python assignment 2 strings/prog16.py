#  Write a Python program to print the index of the character in a string.
string=input("enter the strings")
for index,ch in enumerate(string):
    print("character",ch,"position at",index)