def count(s):
    a="aeiou"
    c=0
    for i in s:
        if i in a:
            c=c+1
    return c
n=input().split()
lst=list(n)
p=[]
l=[]
for i in lst:
    p.append(count(i))
q=max(p)
for i in p:
    print(p.count(q))
    break