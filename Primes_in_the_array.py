n=int(input())
lst=list(map(int,input().split()))
l=[]
for i in lst:
    c=0
    for j in range(1,i):
        if i%j==0:
            c+=1
    if c==1:
        l.append(i)
print(len(l))