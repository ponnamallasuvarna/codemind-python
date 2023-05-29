def count(n):
    c=[]
    if n<0:
        n*=-1
    if n==0:
        return(1)
    while n:
        r=n%10
        c.append(r)
        n=n//10
    r=len(c)
    return r
n=int(input())
lst=list(map(int,input().split()))
l=[]
for i in lst:
    l.append(count(i))
    print(count(i),end=" ")
