def count(n):
    temp=n
    p=n[::-1]
    if p==temp:
        return True
    return False
s=input().lower().split()
l=list(s)
c=0
for i in l:
    if count(i):
        c=c+1
print(c)