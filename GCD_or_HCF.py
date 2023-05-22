n,m=map(int,input().split())
l=[]
k=[]
for i in range(1,n+1):
    if n%i==0:
        l.append(i)
for i in range(1,m+1):
    if m%i==0:
        k.append(i)
a=set(l)
b=set(k)
c=list(a.intersection(b))
print(max(c))