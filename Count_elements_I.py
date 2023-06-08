n,m=map(int,input().split())
lst=list(map(int,input().split()))
l=list(map(int,input().split()))
b=set(lst)
a=set(l)
m=0
p=a.intersection(b)
q=list(p)
for i in q:
    m+=1
print(m)