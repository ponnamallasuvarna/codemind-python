n,m=map(int,input().split())
lst=list(map(int,input().split()))
l=list(map(int,input().split()))
p=set(lst)
q=set(l)
m=[]
t=p.intersection(q)
q=list(p)
for i in lst:
    if i in t:
        m.append(i)
k=[]
for i in m:
    if i not in k:
        k.append(i)
print(*k)