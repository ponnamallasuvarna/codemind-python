def count(s):
    a="aeiou"
    c=0
    for i in s:
        if i in a:
            c=c+1
    return c
n=input().split()
p=list(n)
for i in p:
    print(count(i),end=" ")