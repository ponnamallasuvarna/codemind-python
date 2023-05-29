def count(a):
    b=len(a)
    return b
n=input().split()
lst=list(n)
l=[]
for i in lst:
    l.append(count(i))
print(min(l))