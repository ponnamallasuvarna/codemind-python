s=input().split()
lst=list(s)
i=len(s)
l=[]
while i!=0:
    l.append(lst[i-1])
    i=i-1
print(*l)