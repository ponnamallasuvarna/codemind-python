def count(n):
    p=max(n)
    s=min(n)
    return abs(ord(p)-ord(s))
u=input().split()
v=list(u)
for i in v:
    print(count(i),end=" ")