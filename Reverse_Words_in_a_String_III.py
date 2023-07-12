def rev(n):
    p=n[::-1]
    return p
s=input().split()
l=list(s)
for i in l:
    print(rev(i),end=" ")