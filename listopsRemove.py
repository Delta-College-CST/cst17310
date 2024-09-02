# This program demonstrates various Python list functions
# mainly that remove elements

airports = ["MBS", "DTW", "FNT", "LAN"]    # List of airport codes

airports.remove("LAN")                     # Remove LAN

print(airports)

airports.extend(["TVC","YYZ","JFK"])       # Append list to end

print(airports)

europeair = ["BHX","CDG","AMS"]

airports = airports + europeair            # Append another list to end

print(airports)

deleted = airports.pop(6)                  # Remove element at position 6

print(deleted)                             # Print retrieved element from deletion

print(airports)

airports.clear()                           # Clear all elements from list

print(airports)
