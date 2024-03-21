def somma(n):
    if n==0:
        return 0
    else:
        return somma(n-1)+n
    
print(somma(10))


def somma(n):
    totale=0
    for i in range(n):
        totale+=1
    return totale
print(somma(10))

def Prodotto(n):
    totale=1
    for i in range(n):
        totale*=1
    return totale
print(Prodotto(10))

l=[1,5,4,6,7,6,4,3,2]
totale=0
for i in l:
    totale = totale+i
print(totale)

ls=["Uno", "due", "tre", "quattro"]
#calcolare la somma delle lunghezze delle stringhe
totale=0
for s in ls:
    totale=totale+len(s)
print(totale)

ls=[1,[2,3],3,"ciao","ok", ["a","b"]]
#contare quante stringhe sono presenti nella lista ls
totale=0
tipostringa= type("")
for i in ls:
    if type(i) == tipostringa:
        totale=totale+1
    print(totale)