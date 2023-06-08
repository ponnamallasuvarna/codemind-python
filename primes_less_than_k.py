n=int(input())
lst=list(map(int,input().split()))
m=int(input())
c=0
p=0
l=[]
for i in lst:
    c=0
    for j in range(1,i):
        if i%j==0:
            c+=1
    if c==1:
        l.append(i)
for i in l:
    if i<=m:
        p+=1
print(p)