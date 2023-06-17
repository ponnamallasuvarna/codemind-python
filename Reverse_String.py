s=input().split()
l=list(s)
i=len(s)
li=[]
while i!=0:
    li.append(l[i-1])
    i-=1
print(*li)