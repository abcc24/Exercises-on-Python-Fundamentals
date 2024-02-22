a=print

x, y, z = "Superman", "Spiderman", "Batman"
a (x,y,z)

l, m, n = "Oggi è una bella giornata", "per andare a portare il cane", "al parco sotto casa"
a (l,m,n)

#"a" diventa la funzione print, quindi quando si va a usare print si usa "a" come funzione in questo caso

books = ["lotr", "potter", "throne"]
x, y, z = books
print(x)
print(y)
print(z)

#posso inserire con le parentesi quadre più di una variabile e creare un gruppo

l = [1, 2, 3, 4, 5, "sei" "sette", 8, [9,10,11], "dodici"]
for v in l: #stampa tutti i numeri e le stringhe nella lista indicata come l
    print(v)

for l in range(10): #range(numero) significa fino a quale numero stampa il calcolo
    print(l)

for l in range(4, 20, 3): #i tre nuemri indicano start, stop e step
    print(l)


print(len("Ciao"))
print(len([1,2,3,4,5,6,1,3,2,1]))
#con len si calcola la lunghezza

a=[1]
a.append(2)
print(a)
#.append() va ad aggiungere il valore tra parentesi con quello che stava in precedenza

a.sort()#.sort() va a ordinare il valore tra parentesi con quello che stava in precedenza
print(a)

a.pop()
print(a)#.pop() toglie l'ultimo elemento


#In una stanza entrano, uno dopo l'altro, 10 persone, rispettivamente:
#antonio, marco, andrea, luigi, tony, bruno, laura, anita, annarita, lucia
#le prime due vanno via dopo un pochino di tempo ma entrano altre tre persone
#john, alice, mary
#altre due vanno via, sempre in ordine di ingresso (primo entrato, primo a uscire)
#stampare l'elenco delle persone presenti
#infine, stampare le persone presenti in ordine alfabetico

lista=["antonio", "marco", "andrea", "luigi", "tony", "bruno", "laura", "anita", "annarita", "lucia"]
lista.pop(0) #ricordati che la lista comincia SEMPRE da 0
lista.pop(0) #la posizione di marco diventa 0 perché antonio è stato eliminato nella prima operazione
lista.append("john")
lista.append("alice")
lista.append("mary")
lista.pop(0)
lista.pop(0)
print (lista)
lista.sort()
print (lista)