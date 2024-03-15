# Leggere da un file (persone.txt) i nomi, cognomi e età di un gruppo di persone. 
#organizzarli in un dizionario la cui chiave è il cognome e il cui valore è una tupla contenente i tre valori letti.

fin=open("persone.csv", "r")
linea=fin.readlines()
fin.close

for x in linea:
    l=x.strip().split(",")
    print ("nome: ", l[0], "cognome: ", l[1], "età: ", l[2])


#costruzione dizionario

dizionario=dict()
for x in linea:
    l=x.strip().split(",")
    dizionario[l[1]]= (l[0], l[1], l[2])
    print (dizionario)

for e in dizionario:
    print("Key: ", e, "Value: ", dizionario[e])
