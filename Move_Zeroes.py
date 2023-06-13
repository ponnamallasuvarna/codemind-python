n=int(input())
li=list(map(int,input().split()))
l=[]
p=[]
for i in range(0,len(li)):
    if li[i]==0:
        l.append(li[i])
for j in range(0,len(li)):
    if li[j]!=0:
        p.append(li[j])
r=p+l
print(*r)