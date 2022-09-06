# Write a Python program to swap comma and dot in a string.
# Sample string: "32.054,23"
# Expected list: "32,054.23"

string = input("enter the number with dot and comma to replace dot and comma")
list = []

for i in range(len(string)):
    if string[i] == ".":
        list.append(",")
    elif string[i] == ",":
        list.append(".")
    else:
        list.append(string[i])
#print(list)
print("".join(list))