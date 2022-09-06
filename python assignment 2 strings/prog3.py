# # Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string. 
# Sample String : 'thisisniceone'
# Expected Result : 'thne”'
# Sample String : 'ab'
# Expected Result : 'abab'
# Sample String : 'f'
# Expected Result ab: Empty String 

def first_2_last_2(str):
    if len(str)<2:
        return ''

    return str[0:2] +str[-2:]

strings=input("enetr the strings to print first 2 letter and last 2 letters")
print(first_2_last_2(strings))
