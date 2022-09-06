#  Write a Python function to reverses a string if it's length is a multiple of 4. 
str=input("enter the strings ")
#print(reversed(str))
if len(str) % 4 == 0:
       print("length of the string is multiple of 4 hence the result is:",str[::-1])
else:
    print("length of the string is not  amultiple of 4:",str)