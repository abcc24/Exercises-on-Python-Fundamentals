import json

filejson = open("all-world-cup-players.json", "r")
worldcup = json.load(filejson)
filejson.close()

print(len(worldcup))



quantiCalciatori = dict()
for x in worldcup:
    if x["Team"] in quantiCalciatori.keys():
        quantiCalciatori[x["Team"]]=quantiCalciatori[x["Team"]]+1
    else:
        quantiCalciatori[x["Team"]]=1

print(quantiCalciatori)


#es 1
quantiCalciatori = dict()
for x in worldcup:
    if x["Team"]=="Italy" in quantiCalciatori.keys():
        quantiCalciatori[x["Team"]]=quantiCalciatori[x["Team"]]+1
    else:
        quantiCalciatori[x["Team"]]=1

print("Numero giocatori Italia: "  + str(quantiCalciatori.get("Italy")))
#.get ti fa estrapolare soltanto il valore che viene indicato all'interno della parentesi.
#il valore deve trovarsi naturalmente all'interno del file.

#es 2
quantiCalciatori = dict()
for y in worldcup:
    if y["Team"]=="Brazil" in quantiCalciatori.keys():
        quantiCalciatori[y["Team"]]=quantiCalciatori[y["Team"]]+1
    else:
        quantiCalciatori[y["Team"]]=1

print("Numero giocatori Brasile: "  + str(quantiCalciatori.get("Brazil")))

#es 3
quantiCalciatori = dict()
for z in worldcup:
    if z["Team"]=="Argentina" in quantiCalciatori.keys():
        quantiCalciatori[z["Team"]]=quantiCalciatori[z["Team"]]+1
    else:
        quantiCalciatori[z["Team"]]=1

print("Numero giocatori Argentina: "  + str(quantiCalciatori.get("Argentina")))

#es 4 (?)
quantiCalciatori = dict()
for it in worldcup:
    if it["Team"]=="Italy" and it["Team"]=="Brazil" in quantiCalciatori.keys():
        quantiCalciatori[it["Team"]]=quantiCalciatori[it["Team"]]+1
    else:
        quantiCalciatori[it["Team"]]=1

print("Giocatori che hanno giocato sia per It che per Bz: " + str(quantiCalciatori.get("Team")))


#es 6
old = dict()

for ol in worldcup:
    younger="DateOfBirth"
    if ol["DateOfBirth"] in old.keys():
        ol["DateOfBirth"]>younger
        younger=ol
    
print(ol)