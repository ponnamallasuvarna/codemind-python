t=int(input())
for i in range(t):
    n=int(input())
    li=list(map(int,input().split()))
    l=[]
    for i in range(1,n+1):
        l.append(i)
    for i in l:
        if i not in li:
            print(i)