def length(n):
    l=list(n)
    p="aeiouAEIOU"
    c=0
    if l[0] in p and l[-1] not in p:
        c=c+1
    return c
s=input().split()
k=list(s)
lst=[]
for i in k:
    lst.append(length(i))
print(sum(lst))