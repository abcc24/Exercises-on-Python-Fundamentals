s="alfa;beta;gamma"
#come posso ottenere la lista ["alfa", "beta", "gamma"]?
print (s.split(";"))

#dato alice.txt, stampare, una per riga, tutte le parole che la compongono

fin=open("alice.txt", "r") #aprio il file
linee=fin.readlines() #calcola quante linne ha il file
fin.close #chiude il file
l=[] #indica la lista che verrà usata per indicare tutte le parole
for l1 in linee: #per ogni elemento (l1) nella lista (linee)
    l.extend(l1.split(" ")) #estendi la lista "l" con gli elementi che stanno in linee (l1) che vengono splittati
print (l)                   #con la funzione .split. aggiungi uno spazio " " per indicare che deve splittare dove c'è uno spazio


filter #ammette in ingresso un oggetto (lista, collezione,...) e una funzione
       #torna una collezione di tutti gli elementi che hanno eliminato il False


def Maiuscola(c):
    return c.isupper() #si indica qui se il carattere è maiuscolo

s="Nel mezzo del Cammin di nostra vita"
print (list(filter(Maiuscola,s)))

l=[1,2,3,4,5,6,7,8,9,10,11,12]

def Pari(n):
    return n%2==0

print (list(filter(Pari, l))) #indica tutti i numeri pari togliendo così i dispari

#data una lista di stringhe eliminare dalla lista tutte le stringhe vuote

ls=["uno", "", "due", "tre", "", " ", "", "", "fine"]
lv=[]
for x in ls:
    if len(x.strip())>0: #con strip non tiene conto anche degli spazi con un elemento spazio
        lv.append(x)
print (lv)


#contare quanti caratteri ci sono in alice.txt. poi contare quanti caratteri non spazi bianchi
#invine contare quanti sono i caratteri alphanumerici

fin=open("alice.txt", "r")
linea=fin.read()
caratteri=len(linea)
print (caratteri)

carnonspazi=0
for w in linea:
    if w!=" ":
        carnonspazi+=1
print (carnonspazi)

alfanum=0
for w in linea:
    if w.isalnum():
        alfanum+=1
print (alfanum)

