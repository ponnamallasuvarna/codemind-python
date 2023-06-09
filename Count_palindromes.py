def reverse(s):
    p=str(s)
    q=p[::-1]
    if p==q:
        return True
    else:
        return False
n=int(input())
lst=list(map(int,input().split()))
c=0
for i in lst:
    if reverse(i):
        c+=1
print(c)