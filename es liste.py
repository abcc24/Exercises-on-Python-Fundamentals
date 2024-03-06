lista=["acqua", "fuoco", "vento", "zorro", "gojo", "jojo"]

print (lista[2])

print (lista[0])

print (lista[-1])

print (lista[-2])

print (lista [2:5])

print (lista [:5])

lista[0]="merda"

print (lista)

lista[1:3]="torrone", "albero", "palla"

print (lista)

lista.append ("torrone")

print (lista)

lista.insert (1, "erba")

print (lista)

dnd=["wizard", "rogue", "cleric", "warrior"]

lista.extend (dnd)

print (lista)



#ESERCIZI LISTE

#Print the second item in the fruits list.
fruits = ["apple", "banana", "cherry"]
print(fruits[1])

#Change the value from "apple" to "kiwi", in the fruits list.
fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"
print(fruits)

#Use the append method to add "orange" to the fruits list.
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)

#Use the insert method to add "lemon" as the second item in the fruits list.
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon")
print(fruits)

#Use the remove method to remove "banana" from the fruits list.
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana") #oppure fruits.remove(fruits[1])
print(fruits)

#Use negative indexing to print the last item in the list. 
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])

#Use a range of indexes to print the third, fourth, and fifth item in the list. 
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print (fruits[2:5])

#Use the correct syntax to print the number of items in the list. 
fruits = ["apple", "banana", "cherry"]
print (len(fruits))


#List objects have a sort() method that will sort the list alphanumerically, ascending, by default:
#Sort the list alphabetically:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

#To sort descending, use the keyword argument reverse = True:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

#Make a copy of a list with the copy() method:
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#Join two list:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

#Use the extend() method to add list2 at the end of list1:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1) 