#ESERCIZI TUPLES

#Use the correct syntax to print the first item in the fruits tuple.
fruits = ("apple", "banana", "cherry")
print (fruits[0])

#Use the correct syntax to print the number of items in the fruits tuple.
fruits = ("apple", "banana", "cherry")
print (len(fruits))

#Use negative indexing to print the last item in the tuple. 
fruits = ("apple", "banana", "cherry")
print (fruits[-1])

#Use a range of indexes to print the third, fourth, and fifth item in the tuple. 
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print (fruits[2:5])




#One item tuple, remember the comma:
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))





#The tuple() Constructor

#It is also possible to use the tuple() constructor to make a tuple.
#Example:

#Using the tuple() method to make a tuple:
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)