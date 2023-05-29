def count(n):
    c=[]
    while n:
        r=n%10
        c.append(i)
        n=n//10
    t=len(c)
    return t
n=int(input())
lst=list(map(int,input().split()))
l=[]
for i in lst:
    l.append(count(i))
q=min(l)
for i in l:
    print(l.count(q))
    break