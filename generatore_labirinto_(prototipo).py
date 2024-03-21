import random

labirinto=[]
labitinto2=[]
labirinto3=[]
labirinto4=[]
labirinto5=[]
labirinto6=[]
labirinto7=[]

for i in range (6):
    labirinto=random.randint (0,6)

if labirinto>=6:
    for l6 in range(2):
        labirinto2=random.randint(0,2)
        if labirinto2==1:
            print ("stanza buia con mostro")
        else:
            print("stanza buia senza mostro")
elif labirinto>=5:
    for l5 in range(2):
        labirinto3=random.randint(0,2)
        if labirinto3==1:
            print ("trappola normale")
        else:
            print("trappola stronza")
elif labirinto>=4:
    for l4 in range(2):
        labirinto4=random.randint(0,2)
        if labirinto4==1:
            print ("corridoio verde")
        else:
            print("corridoio rosso")
elif labirinto>=3:
    for l3 in range(2):
        labirinto5=random.randint(0,2)
        if labirinto5==1:
            print ("sala del trono")
        else:
            print("sala da pranzo")
elif labirinto>=2:
    for l2 in range(2):
        labirinto6=random.randint(0,2)
        if labirinto6==1:
            print ("compare un drago")
        else:
            print("compare uno stronzo")
elif labirinto>=1:
    for l1 in range(2):
        labirinto7=random.randint(0,2)
        if labirinto7==1:
            print ("trovi una pozione")
        else:
            print("trovi una spada")