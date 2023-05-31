def count(n):
    p=max(n)
    return ord(p)
def counts(n):
    s=min(n)
    return ord(s)
u=input().split()
lst=list(u)
v=[]
for i in lst:
    v.append(count(i))
    v.append(counts(i))
u=0
a=0
for i in range(0,len(v)):
    if i%2==0:
        u+=v[i]
    else:
        a+=v[i]
print(u-a)