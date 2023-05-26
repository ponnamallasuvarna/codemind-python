n=int(input())
lst=list(map(int,input().split()))
l=[]
m=[]
p=""
q=""
for i in lst:
    if i%2!=0:
        l.append(i)
for i in lst:
    if i%2==0:
        m.append(i)
s=l+m
print(*s)