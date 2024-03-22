#cosa faremo oggi?
#un esempio di progetto segmentato

#sia data una lista <ls> contenente N digit da 1 a N
#non necessariamente tutti presenti quindi con eventuali ripetizioni

#ls=[1,1,2,3,3,5,8,8]

#N=5

#[1,3,5,1,5]

#sia data una seconda lista costruita esattamente come la precedente
#ovviamente con valori diversi, ma sembre nel rispetto del valore N

N=6

ls=[1,1,2,2,5,6]
lscheck=[2,3,3,6,6,4]

#scrivere una funzione ala quale passerete come parametri ls e lscheck
#e la funzione deve riportare 2 valori: il primo tutte le volte che nella stessa posizione
#c'è lo stesso digit nella stessa posizione di ls e lscheck
#sarà 1
#A questo punto per completare il calcolo tolgo dalle due liste
#i valori che stanno nella stessa posizione
#il secondo tutte le volte in cui un elemento della lista lscheck è presente nella lista ls
#ma non nella stessa posizione
#c'è il 2 nella ls?
#sì, lo tolgo

ls=[2,2,5]
lscheck=[2,3,6,6,4]

import random

#genera una lista che contiene N digit casuali tra 1 e N
def GeneraLista(N):

    lista1=[]

    for i in range(N):
        v=random.randint(1,N)
        lista1.append(v)
    return lista1
print(GeneraLista(10))


def ContaUguali(a,b): #quando si mette def tutto quello che c'è scritto prima non valgono

    ug=0

    for i in range(len(a)):
        if a[i]==b[i]:
            ug=ug+1
        return ug
print(ContaUguali(ls,lscheck))
            

#vedere se un numero è compreso almeno una volta nell'altra vista non nello stesso posto
            
l2=[1, 1, 4, 3, 1]
l3=[4, 2, 1, 3, 2]
2 (4,1), 1
[5, 5, 3, 1, 4]
[5, 4, 2, 5, 5]
2 (5,4), 2
[5, 1, 3, 2, 4]
[1, 5, 4, 4, 2]
4 (1,5,4,2) ,0
[3, 2, 3, 4, 5]
[1, 5, 4, 5, 5]
1 (4), 1

def contaugualiinaltroposto(ls, lscheck):
    ls = ls.copy()
    lsCheck = lsCheck.copy()
    ls=[1,1,4,3,1]
    lscheck=[1,4,1,4,3]
    #conteggio ed elimino gli elementi nello stesso posto
    stessoposto=0
    for i in range(len(lscheck)):
        if lscheck[i]==ls[i]:
            stessoposto+=1
            ls[i]=None
            lscheck=[i]=None
    
    #contengo ed elimino gli elementi in un posto differente
    altroposto=0
    for i in range(len(lscheck)):
        if lscheck[i]!=ls[i]:
            altroposto+=1
            ls[i]=None
            lscheck[i]=None
    return stessoposto, altroposto

