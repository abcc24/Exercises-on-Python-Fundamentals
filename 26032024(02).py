import copy
import random

def ConvertiStringaDigitInListaNumeri(sd):
    return [int(x) for x in list(sd)]

def GeneraLista(N, M):
    lista = []
    for i in range(M):
        v = random.randint(1, N)
        lista.append(v)
    return lista

N = int(input("Inserire il numero di simboli: "))
M = int(input("Inserire la lunghezza della lista: "))
print(GeneraLista(N,M))