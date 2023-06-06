n=int(input())
li=list(map(int,input().split()))
l=[]
m=[]
p=1
h=1
for i in li:
    c=0
    for j in range(1,i):
        if i%j==0:
            c+=1
    if c==1:
        l.append(i)
    else:
        m.append(i)
for i in l:
    p=p*i
for i in m:
    h=h*i
print(h-p)
        