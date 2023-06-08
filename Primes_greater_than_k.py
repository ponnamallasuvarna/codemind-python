n=int(input())
lst=list(map(int,input().split()))
m=int(input())
l=[]
p=0
for i in lst:
    c=0
    for j in range(1,i+1):
        if i%j==0:
            c+=1
    if c==2:
        l.append(i)
for i in l:
    if i>=m:
        p+=1
print(p)