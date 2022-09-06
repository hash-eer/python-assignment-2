# Write a Python program to count repeated characters in a string.
# Sample string: 'thequickbrownfoxjumpsoverthelazydog'
# Expected output :
# o 4
# e 3
# u 2
# h 2
# r 2
# t 2

string = input("enter the string")
for i in range(0,len(string)):
    count=1
    for j in range(i+1,len(string)):
        if string[i]==string[j] :
            count=count+1
            string = string[:j]+'0'+string[j+1:]
    if (count>1 and string[i]!='0'):
        print(string[i],"",count)
        
        
