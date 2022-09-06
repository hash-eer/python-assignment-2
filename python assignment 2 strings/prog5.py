# Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
# Sample String : 'abc', 'xyz' 
# Expected Result : 'xyc abz'

str1=input("enter the first strings  to mix up")
str2=input("enter the second strings  to mix up")

new_str1=str2[:-1] + str1[-1:]
new_str2=str1[:-1] + str2[-1:]

print(new_str1+' '+new_str2)