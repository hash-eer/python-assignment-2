# Write a Python program to remove the nth index character from a nonempty string

str=input("enter the words:")
n=int(input("enter the index to reve the letters:"))
print("after removing the character from the given index the result is :",str[:n] +str[n+1:])
