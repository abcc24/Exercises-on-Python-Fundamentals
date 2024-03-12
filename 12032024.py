var=10
nome=0
numero="Altro"

ottimo=[1,2,3,4,5]
esempio=["uno", nome, var, ottimo]
print (esempio)
nome="nome proprio"
print (esempio)
ottimo.append (1000)
print (esempio)
ottimo=100000
print (esempio)
nome=123
print (esempio)

a=[1,2,3,4]
b=a
a=100
print(b)

a=["uno",[1,2,3]]
b=a
a[1].append (1000)
a="Ciao"
print (b)

a=[1,2,3]
b=[4,5,6]
c=[a,b]
d=[a,b,c]
a[2]=0
b[1]=1
c[0]=999
print (d)
exit(-1)
