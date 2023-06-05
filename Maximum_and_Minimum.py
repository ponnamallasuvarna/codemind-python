n=int(input())
li=list(map(int,input().split()))
d={}
for i in li:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
l=[]
for i in d:
    if i==d[i]:
        l.append(i)
if len(l)!=0:
    print(min(l),max(l))
else:
    print("-1")
        