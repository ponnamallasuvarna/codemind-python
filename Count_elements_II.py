n,m=map(int,input().split())
lst=list(map(int,input().split()))
l=list(map(int,input().split()))
b=set(lst)
a=set(l)
q=[]
s=[]
r=[]
o=0
p=a.intersection(b)
q=list(p)
for j in lst:
    if j not in q and j in lst:
        s.append(j)
for i in l:
    if i not in q and i in l:
        s.append(i)
r=set(s)
for h in r:
    o+=1
print(o)