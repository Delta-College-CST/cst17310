# This program demonstrates various Python list functions
# mainly that add elements

hours = [ 4, 3, 5, 6 ]

print(hours)

hours.append(2)            # Add element 2 at end of list

hours.insert(2,1)          # Insert 1 at position 2

print(hours)

morehours = [11, 22, 33]

hours.extend(morehours)    # Append morehours to end of hours

print(hours)
						
