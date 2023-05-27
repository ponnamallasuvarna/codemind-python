def count(l):
    for i in range(0,len(l)-1):
        if l[i]>l[i+1]:
            return False
            break
    else:
        return True
r,c=map(int,input().split())
k=[]
for i in range(r):
    x=list(map(int,input().split()))
    k.append(x)
m=[]
for i in range(c):
    s=[]
    for j in range(r):
        s.append(k[j][i])
    m.append(s)
c=0
for i in m:
    if count(i):
        c=c+1
print(c)