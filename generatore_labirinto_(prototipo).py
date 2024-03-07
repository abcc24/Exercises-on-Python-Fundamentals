import random

labirinto=[]

for i in range (6):
    labirinto=random.randint (0,6)

if labirinto>=6:
    print ("stanza buia")
elif labirinto>=5:
    print ("trappola")
elif labirinto>=4:
    print ("corridoio")
elif labirinto>=3:
    print ("sala del trono")
elif labirinto>=2:
    print ("compare un mostro")
elif labirinto>=1:
    print ("compare un mostro")