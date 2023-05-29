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
for i in lst:
    p.append(count(i))
print(min(p))
    