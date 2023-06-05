n=int(input())
lst=list(map(int,input().split()))
i=0
j=-1
l=[]
while i!=len(lst) and j!=0 and j!=-(len(lst)//2)-1:
    l.append(lst[i])
    l.append(lst[j])
    j=j-1
    i=i+1
if n%2!=0:
    p=len(lst)//2
    l.append(lst[p])
    l.append(0)
print(*l)