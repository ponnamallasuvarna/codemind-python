t=int(input())
l=[]
for i in range(t):
    n=int(input())
    l.append(n)
k=int(input())
c=0
for i in l:
    if i>k:
        c=c+1
print(len(l)+c)