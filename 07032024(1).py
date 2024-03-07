print (hash("Mario"))# La funzione hash() restituisce il valore di hash di un oggetto con un numero.

print (hash("Mario")%17)
#con il calcolo del modulo (%) 17 (sono 16 i posti + 1) per far rientrare il numero dato dal primo print in 16 posti.

print (hash("Rossi")%17)
print (hash("Verdi")%17)
print (hash("Bianchi")%17)
print (hash("Neri")%17)
print (hash("Bianchini")%17)



#Comprehension
lista=[1,2,3,4,5]

lista2=[x*x for x in lista]
print (lista2)

#oppure si può scrivere così
lista2=[]
for x in lista:
    lista2.append(x*x)
print (lista2)



lista=[2,3,4]
lista3=[y for x in lista for y in range(1,x)]
print (lista3)



#funzione zip accosta due elementi
lista_dispari = [x*2+1 for x in range (0,10)]
lista_numeri = [x for x in range (0,10)]
print (lista_dispari)
print (lista_numeri)
print(list(zip(lista_numeri, lista_dispari)))

nomi=["mario", "bianco", "verde"]
cognomi=["rossi", "bianchi", "verdi"]
print (list(zip(nomi, cognomi)))