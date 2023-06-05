n=int(input())
lst=list(map(int,input().split()))
a=sum(lst)
b=len(lst)
c=a//b
ct=0
for i in lst:
    if i<=c:
        ct=ct+1
    else:
        pass
print(ct)