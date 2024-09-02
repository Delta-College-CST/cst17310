# This program demonstrates various basic Python list actions

infolist = [ 4, 3, 5, 6, 2, 8, 1 ]  # Declare an initialize a list

print(infolist)                     # Print list contents

print(infolist[0])                  # Access list elements - first
print(infolist[3])                  # Access list elements - 4th
print(infolist[6])                  # Access list elements - last

listLength = len(infolist)          # Access
print(listLength)                   # and print list length      

for listItem in infolist:           # Iterate through list and
    print(listItem,end=' ')         # print on same line
print()

newList = infolist[1:4]             # Splice to create sublist
print(newList)                      # positions 1-4 (2nd-5th elements)
