n=int(input())
lst=list(map(int,input().split()))
l=[]
m=[]
for i in lst:
    if i%2==0:
        l.append(i)
for i in lst:
    if i%2!=0:
        m.append(i)
print(*(l+m))