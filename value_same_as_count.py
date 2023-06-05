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
    if d[i]==i:
        l.append(i)
print(len(l))
