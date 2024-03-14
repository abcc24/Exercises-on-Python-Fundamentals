lista1=[0,9,8,7,6]
lista2=[3,1,5,4,7,6,11]

for lista2 in lista1: #lista2 era per forviare. nell'operazione for "lista 2" prende tutti gli elementi di lista 1 
    print(lista2)


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
def sdl (s):
    lista=[]
    for i in s:
        lista.append(int(i))
    return lista
print (sdl("3456"))

##################################################################

def GeneraListaDigit():
    lista=[]
    for i in range (0,10000):
        s = str(i)
        s=s.zfill(4) #sipuò fare anche con zfill per dare la lunghezza necessaria alla stringa
        lista.append(s)
    return lista
print (GeneraListaDigit())


#problema: ho la stringa "123", la voglio trasformare in [1,2,3]
#definire una funzione che risolve il problema

def stringatolista(aa):
    lista=[]
    for x in aa:
        lista.append(int(x))
    return lista #ripete l'operazione di for per ogni elemento che sta inserito nella stringa "123" che sta su print
print (stringatolista("123"))

def stringarolista (aa): #secondo metodo
    l=list(aa)
    l1=[]
    for i in l:
        l1.append(int(i))
    return l1
print (stringarolista("123"))

def stringatolista (aa):
    return [int(x) for x in list(aa)] #terzo metodo
print (stringatolista("123"))

####################################################################

#Apertura dei file

fin=open("alice.txt", "r") #apre un file, in questo caso il file alice. r vuol dire che si apre in letura
#w per scrivere e a per appendere
linee=fin.readlines() #legge tutte le linee
fin.close() #per chiudere il file
print(linee)

#come faccio a togliere questi fine riga (il carattere a capo)?

l1=[]
print(l1)
for l in linee:
    l1.append(l.strip()) #elimina spazi, tab e eol ma solo a inizio e alla fine della riga
print(l1)

s="alfa;beta;gamma"
#come posso ottenere la lista ["alfa", "beta", "gamma"]?
print (s.split(";"))

#dato alice.txt, stampare, una per riga, tutte le parole che la compongono
