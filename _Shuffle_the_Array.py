n=int(input())
li=list(map(int,input().split()))
m=int(input())
l=[]
k=[]
for i in range(0,m):
        l.append(li[i])
for i in range(m,len(li)):
    k.append(li[i])
i=0
j=0
h=[]
while i!=len(l) and j!=len(k):
    h.append(l[i])
    h.append(k[i])
    i+=1
    j+=1
print(*h)