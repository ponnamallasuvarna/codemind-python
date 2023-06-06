t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    l.sort(reverse=True)
    i=0
    j=-1
    lst=[]
    while i!=len(l) and j!=0 and j!=-(len(l)//2)-1:
        lst.append(l[i])
        lst.append(l[j])
        i+=1
        j-=1
    t=[]
    t.append((l[len(l)//2]))
    if len(l)%2==0:
        print(*lst)
    else:
        print(*((lst)+t))