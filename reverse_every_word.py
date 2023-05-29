def reverse(n):
    p=n[::-1]
    return p
s=input().split()
p=list(s)
for i in p:
    print(reverse(i),end=" ")