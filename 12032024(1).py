a=10
b=20
c=30

#se a è pari, stampo b+c
#se a è dispari stampo b-c

if a % 2 == 0: #verifica che a è pari (0 è considerato pari con i numeri binari, mentre 1 è dispari)
    #si può scrivere anche if a & 1 == 0:
    #come terzo modo abbiamo math.floor(a/2)*2==a
    print (b+c)


#supponiamo di aver scelto la tecnica del modulo
    
a=10
b=20
c=30

if a%2==0:
    print(b+c)
else:
    print(b-c)

a=13
b=7
c=2

if a%2==0:
    print(b+c)
else:
    print(b-c)

a=int (input())
b=int (input())
c=int (input())
if a%2==0:
    print(b+c)
else:
    print(b-c)

#come posso evitare di copiare di continuo
#sempre lo stesso pezzo di codice?
#Le Funzioni:
def Arit(a,b,c): 
    d=100 #una variabile definita in una funzione non è visibile dall'esterno
    if a%2==0:
        print(b+c)
    else:
        print(b-c)

Arit(10,11,12)
Arit(11,2,3)
Arit(101,1000,2)
a,b,c=10,20,30
Arit(b,c,a)

#a,b,c sono parametri formali (il valore sarà a tempo di chiamata di funzione)

def cambia(a,b):
    a=b
    print(a)

a=100 #questo non ha nulla a che vedere con la a all'interno della funzione sopra (def cambia(a,b):)
b=200
cambia (a,b)
print(a)

def somma (a,b):
    c=a+b
    return c
print(somma(1,2))
print(somma("a", "b"))

a,b,c=1,2,3

def divisione (a,b):
    return a//b, a%b

h,i=a//b,a%b

#scrivere una funzione ColoreCasuale() che torna una stringa casuale tra "rosso", "giallo", "verde", "blu", "arancio"...

import random

def ColoreCasuale (): #indica che con ci sono parametri per ColoreCasuale
    colori= ["giallo", "rosso", "verde", "blu", "arancio"]
    return colori[random.randint (0, len(colori)-1)] #ritorna tra i "colori" un colore tra 0 e l'ultimo

print (ColoreCasuale())

#questa funzione trova il numero maggiore della lista

def Maggiore(lista):
    if len(lista)==0:
        return None
    else:
        magg=lista[0]
        for i in lista[1:]:
            if magg<i:
                magg=i
        return magg
print (Maggiore([2,5,9,10,45,679,345,231,5555]))

#ricordate che un digit è uno tra 0,1,2,3,4,5,6,7,8,9
#Problema: scrivere una funzione che costituisce una lista
#contenente tutte le possibili combinazioni in quattro digit.

def GeneraListaDigit():
    lista=[]
    for i in range (0,10000):
        s = str(i)
        while len(s) < 4:
            s="0"+s
        lista.append(s)
    return lista

print (GeneraListaDigit())

#modificare la GeneraListaDigit per generare una lista di liste del tipo
#[0,0,0,0], [0,0,0,1], [0,0,0,2], ... ,[9,9,9,8], [9,9,9,9]

def GeneraListaDigit():
    lista=[]
    for i in range (0,10000):
        s = str(i)
        while len(s) < 4:
            s="0"+s
            #devo modificare s in lista di digit s, esempio è "3410" => [3,4,1,0]
        lista.append(s)
    return lista

print (GeneraListaDigit())

#data una stringa numerica (es: "98123"), convertirla in una lista di digit [9,8,1,2,3]
def sdl ():
    stringa=()
    for i in stringa (range(0,1000)):
        c=int(i)
        stringa.append(c)
print (c)