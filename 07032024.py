import random
import time

#LISTE

start=time.time_ns()# time_ns è il tempo in nano secondi, calcola quindi il tempo trascorso dal 01/01/1970
lista=[]
for v in range(1,10000000):
    lista.append(random.randint(1, 1000000000))
end = time.time_ns()

print(f"Il tempo richiesto è: {(end-start)/1000000000}")



start=time.time_ns()
trovati = 0
for v in range(1,1000):
    if random.randint(1, 1000000000) in lista:
        trovati += 1
end = time.time_ns()

print(f"Il tempo richiesto è per cercare è: {(end-start)/1000000000} e ne ha trovati {trovati}")
#la lista è sequenziale, quindi la complessità della ricerca della lista (il suo tempo) è pari a quanti elementi ci sono nella lista
#la lista è utile per inserire un solo elemento

######################################################################

#SETS

#i sets (insiemi) sono più veloci

start=time.time_ns()
aset = set()
for v in range(1,10000000):
    aset.add(random.randint(1, 1000000000))
end = time.time_ns()

print(f"Il tempo richiesto è: {(end-start)/1000000000}")


start=time.time_ns()
trovati = 0
for v in range(1,1000):
    if random.randint(1, 1000000000) in lista:
        trovati += 1
end = time.time_ns()

print(f"Il tempo richiesto è per cercare è: {(end-start)/1000000000} e ne ha trovati {trovati}")