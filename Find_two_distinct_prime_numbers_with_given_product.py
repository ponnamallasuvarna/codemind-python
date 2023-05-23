n=int(input())
l=[]
p=1
for i in range(2,n):
    if n%i==0:
        l.append(i)
for i in l:
    p=p*i
if p>=n:
    print(*l)
else:
    print("-1")