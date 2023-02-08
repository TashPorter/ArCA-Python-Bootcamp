#my dinner party 
names=["Conrad Anker","Nick Offerman","Rebecca Rusch"]
print(names)
# #replaces value via index
names[0] = "Margo Hayes"
print(names)
# # #append adds to end of list
names.append("Will Ferrell")
print(names)
# # #insert value (must put new value and place)
names.insert(3, "Rainn Wilson")
print(names)
# # # removes the statement at that location
del names [3]
print(names)
# # # removes an item in the list via index (can still use)
names.pop(0)
print(names)
# # #removes one element by value rather than index
names.remove("Rebecca Rusch")
print(names)
#permanetely changes the list to appropriate sorting based on alphabetical order
names.sort
print(names)
#sorts the list based on alphabetical (temporarily)
print(sorted(names))
print(names)

print(id(names))
print(names)
#sorts in reverse (temporarily)
print(sorted(names, reverse=True))
#sorts list in reverse permanetely 
names.sort(reverse=True)
print(names)

print(id(names))
print(names)
print(id(sorted(names, reverse=True)))