n=int(input())
lst=list(map(int,input().split()))
p=[]
for i in lst:
    if lst.count(i)==1:
        p.append(i)
if len(p)==0:
    print("-1")
else:
    print(*p)