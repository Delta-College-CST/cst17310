# This program demonstrates list searching:
#  1) Searching for element existence
#  2) Searching for element index

fruit = ["orange", "mango", "watermelon", "kiwi", "pineapple", "banana"]

# Search for element existence
if "kiwi" in fruit:
    print("YES")
else:
    print("NO")
    
if "grapefruit" in fruit:
    print("YES")
else:
    print("NO")

# Search for element index
i = fruit.index("kiwi")
print(i)

i = fruit.index("orange")
print(i)

i = fruit.index("grapefruit")   # This will crash your program
print(i)
