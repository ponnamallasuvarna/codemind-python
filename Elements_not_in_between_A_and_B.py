n=int(input())
lst=list(map(int,input().split()))
a,b=map(int,input().split())
s=0
l=[]
for i in lst:
    if i<a or i>b:
        l.append(i)
        s=s+i
if len(l)==0:
    print("-1")
else:
    print(*l)