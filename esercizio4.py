numero_intero=24
print (type(numero_intero)) #type identifica il tipo di valore che c'è

numero_decimale=25.5
print (type(numero_decimale))

testo="Correvo nel vuoto"
print (type(testo))

valore=True
print (type(valore))

numeri=[1,2,3,4,5]
print (type(numeri))

faffa=[1,3.5,"elena",False]
print (type(faffa))

numero1=13
numero2=20
numero3=(numero1+numero2)
print(numero3)

differenza=numero2-numero1
print(differenza)

prodotto=numero1*numero2
print(prodotto)

resto=numero2%numero1
print(resto)

risultato1=numero1*(numero1)+5
risultato2=risultato1+(numero2**2)#numero elevato alla seconda si scrive **2
print(risultato2)

risultato=numero1-(numero1-1) #operazione che serve per riportarte un numero a 1
print(risultato)

variabile=("ciao mondo")
variabile_maiuscola = variabile.upper()#con questa operazione di convertono le minuscole con le maiuscole
print(variabile_maiuscola)
#si usa .lower per creare le minuscole

stringa="vado a correre sotto la pioggia perché mi voglio male"
stringa2=stringa.split()
print(stringa2)