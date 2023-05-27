r,c=map(int,input().split())
l=[]
k=[]
p=[]
m=[]
for i in range(r):
    x=list(map(int,input().split()))
    l.append(x)
for i in range(0,len(l),len(l)-1):
    k.append(l[i])
for i in range(1,len(l)-1,1):#1  #2
    p.append(l[i])
#print(p)
for i in p:
    for j in range(0,len(i),len(i)-1):
        m.append(i[j])
#print(sum(m))
a=[]
for i in k:
    for j in i:
        a.append(j)
print(sum(a)+sum(m))