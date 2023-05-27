def reverse(n):
    p=n[::-1]
    return p
s=input().split()
l=list(s)
for i in range(0,len(l)):
    if i%2==0:
        l[i]=reverse(l[i])
    else:
        pass
print(*l)