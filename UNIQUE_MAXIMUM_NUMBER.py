t=int(input())
li=list(map(int,input().split()))
p=[]
for i in li:
    if li.count(i)==1:
        p.append(i)
if len(p)==0:
    print("-1")
else:
    print(max(p))