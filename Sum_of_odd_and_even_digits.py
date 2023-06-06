n=int(input())
li=list(map(int,input().split()))
s=0
p=0
for i in range(0,len(li)):
    if i%2==0:
        s=s+li[i]
    else:
        p=p+li[i]
if p-s==0:
    print("YES")
else:
    print("NO")