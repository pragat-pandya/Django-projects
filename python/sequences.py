################## STRINGS ######################################
# They are non-mutable ordered sequnce.
# They are indexed from 0. and can be accssed using '[]' operator.
# name[start:stop:step]
name = "John Deer"
# Prints the entire string.
print(name)
# prints first(0th) character of string 'name'.
print(name[0])


####################### LISTS ####################################
# They are mutable ordered sequnces of objects any types.
# There are so many useful methods pre-defined in Python to manipulate lists.
# They can be used to store any variable types and can be constructed usign square brackets and commas as following:
names = ["Aplha", "Beta", "Gama", "Theta"]
# prints the entire list.
print(names)
# prints second element namely: "Gamma".
print(names[2])
# Adds a new element at the end of the list.
names.append("Sigma")
# Sorts the list according to the types of the element, in this case it sorts it in the lexicographic order.
names.sort()
# Prints the new sorted list.
print(names)


################ TUPLES ##################################################
# They are non-mutable ordered sequnce of any type (or mixture of sevaral types).
# They are used when we need to group two or three variables under one name as a single unit. eg., for saving coordinates.
cordinate = (10.0, 20.0)
# Prints the entire tuple.
print(cordinate)
# Prints the first element of the tuple (0-based indexing).
print(cordinate[1])


########################### SETS ########################################
# This is an un-ordered collection of objects.
# Python sets are just like the sets from the world of mathametics!
# Initializes an empty set
var = set()
# Add 1 and 2 to set
var.add(1)
var.add(2)
# prints the number of elemets in the set 'var'.
print(len(var))
# removes element provided to the argument of remove.
var.remove(2)
