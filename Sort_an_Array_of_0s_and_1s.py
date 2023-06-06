n=int(input())
lst=list(map(int,input().split()))
a=[]
b=[]
c=0
for i in lst:
    if i==0:
        a.append(i)
for j in lst:
    if j==1:
        b.append(j)
print(*(a+b))