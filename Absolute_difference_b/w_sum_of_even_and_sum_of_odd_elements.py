n=int(input())
li=list(map(int,input().split()))
l=[]
m=[]
for i in(li):
    if i%2==0:
        l.append(i)
for i in(li):
    if i%2!=0:
        m.append(i)
print(abs(sum(l)-sum(m)))